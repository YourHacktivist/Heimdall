"""
OAuth credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_oauth():
    """Generate fake OAuth credentials."""
    return {
        "OAUTH_CLIENT_ID": random_string(24),
        "OAUTH_CLIENT_SECRET": random_string(40),
        "OAUTH_REDIRECT_URI": f"https://{random_domain()}/auth/callback",
        "OAUTH_SCOPE": "read:user,user:email",
        "OAUTH_STATE_SECRET": random_string(32),
        "OAUTH_TOKEN_URL": f"https://{random_domain()}/oauth/token",
        "OAUTH_AUTHORIZE_URL": f"https://{random_domain()}/oauth/authorize"
    }
