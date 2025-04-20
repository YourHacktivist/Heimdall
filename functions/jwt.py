"""
JWT credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_jwt():
    """Generate fake JWT credentials."""
    header_b64 = random_string(36)  # Simulate base64
    payload_b64 = random_string(120)  # Simulate base64
    signature = random_string(43)  # Simulate signature
    
    token = f"{header_b64}.{payload_b64}.{signature}"
    
    return {
        "JWT_SECRET": random_string(48),
        "JWT_PRIVATE_KEY": "-----BEGIN PRIVATE KEY-----\n" + random_string(64) + "\n-----END PRIVATE KEY-----",
        "JWT_PUBLIC_KEY": "-----BEGIN PUBLIC KEY-----\n" + random_string(64) + "\n-----END PUBLIC KEY-----",
        "JWT_TOKEN": token,
        "JWT_ALGORITHM": random.choice(["HS256", "RS256", "ES256"]),
        "JWT_EXPIRES_IN": random.choice(["1h", "12h", "24h", "7d", "30d"]),
        "JWT_ISSUER": random_domain()
    }
