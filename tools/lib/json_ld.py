import json
from tools.lib.verdict import normalize_verdict

REPO_URL = "https://github.com/yaniv-golan/proof-engine"


def generate_claim_review(proof_data: dict, canonical_url: str) -> str:
    verdict_info = normalize_verdict(proof_data["verdict"])

    claim_review = {
        "@context": "https://schema.org",
        "@type": "ClaimReview",
        "claimReviewed": proof_data["claim_natural"],
        "reviewRating": {
            "@type": "Rating",
            "ratingValue": verdict_info["rating"],
            "bestRating": 5,
            "worstRating": 1,
            "alternateName": verdict_info["raw"],
        },
        "author": {
            "@type": "Organization",
            "name": "Proof Engine",
            "url": REPO_URL,
        },
        "datePublished": proof_data["generator"]["generated_at"],
        "url": canonical_url,
    }

    return json.dumps(claim_review, indent=2)
