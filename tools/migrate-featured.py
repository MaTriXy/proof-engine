#!/usr/bin/env python3
"""One-time migration: extract featured flags to site/proofs/featured.json."""

import json
import sys
from pathlib import Path
import yaml

def main():
    site_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("site")
    proofs_dir = site_dir / "proofs"

    if not proofs_dir.is_dir():
        print(f"ERROR: {proofs_dir} not found", file=sys.stderr)
        sys.exit(1)

    featured_slugs = []
    modified_json = []
    modified_yaml = []

    for slug_dir in sorted(proofs_dir.iterdir()):
        if not slug_dir.is_dir():
            continue
        slug = slug_dir.name

        # Check meta.yaml first (current precedence)
        meta_path = slug_dir / "meta.yaml"
        proof_json_path = slug_dir / "proof.json"

        effective_featured = False

        if meta_path.exists():
            meta = yaml.safe_load(meta_path.read_text()) or {}
            if "featured" in meta:
                effective_featured = bool(meta["featured"])
                # Remove from meta.yaml
                del meta["featured"]
                if meta:
                    meta_path.write_text(yaml.dump(meta, default_flow_style=False))
                else:
                    meta_path.unlink()
                modified_yaml.append(slug)
            elif proof_json_path.exists():
                data = json.loads(proof_json_path.read_text())
                if "featured" in data:
                    effective_featured = bool(data["featured"])
        elif proof_json_path.exists():
            data = json.loads(proof_json_path.read_text())
            if "featured" in data:
                effective_featured = bool(data["featured"])

        if effective_featured:
            featured_slugs.append(slug)
            print(f"  FEATURED: {slug}")

        # Remove featured from proof.json regardless
        if proof_json_path.exists():
            data = json.loads(proof_json_path.read_text())
            if "featured" in data:
                del data["featured"]
                proof_json_path.write_text(json.dumps(data, indent=2) + "\n")
                modified_json.append(slug)

    # Write featured.json
    featured_path = proofs_dir / "featured.json"
    featured_path.write_text(json.dumps(sorted(featured_slugs), indent=2) + "\n")

    print(f"\nMigration complete:")
    print(f"  Featured proofs: {len(featured_slugs)}")
    print(f"  proof.json files cleaned: {len(modified_json)}")
    print(f"  meta.yaml files cleaned: {len(modified_yaml)}")
    print(f"  Written: {featured_path}")


if __name__ == "__main__":
    main()
