"""
GitHub credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string

def generate_github():
    """Generate fake GitHub tokens."""
    prefixes = ["ghp_", "gho_", "ghu_", "ghs_", "ghr_"]
    username = random.choice(["dev", "admin", "ci", "bot"]) + random_string(random.randint(4, 10)).lower()
    return {
        "GITHUB_TOKEN": random.choice(prefixes) + random_string(36, string.ascii_letters + string.digits),
        "GITHUB_USERNAME": username,
        "GITHUB_REPO": f"{random_string(random.randint(4, 10)).lower()}-{random_string(random.randint(4, 8)).lower()}",
        "GITHUB_OWNER": random.choice([username, f"{random_string(6).lower()}-org", f"{random_string(6).lower()}-inc"]),
        "GITHUB_WEBHOOK_SECRET": random_string(32, string.ascii_letters + string.digits),
        "GITHUB_APP_ID": str(random.randint(100000, 999999)),
        "GITHUB_APP_PRIVATE_KEY": "-----BEGIN RSA PRIVATE KEY-----\n" + random_string(64) + "\n-----END RSA PRIVATE KEY-----"
    }
