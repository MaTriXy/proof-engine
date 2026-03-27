import sys
import os

# Add proof-engine scripts to path so tests can import them
SCRIPTS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "proof-engine", "skills", "proof-engine"
)
sys.path.insert(0, SCRIPTS_DIR)
