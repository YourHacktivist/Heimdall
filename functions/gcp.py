"""
Google Cloud Platform credential generator for Heimdall.
"""

import random
import string
import json
from functions.utils import random_string, random_domain

def generate_gcp():
    """Generate fake Google Cloud Platform credentials."""
    project_id = f"{random_string(6).lower()}-{random.choice(['app', 'platform', 'project', 'cloud'])}-{random.randint(100000, 999999)}"
    return {
        "GCP_PROJECT_ID": project_id,
        "GCP_SERVICE_ACCOUNT_KEY": json.dumps({
            "type": "service_account",
            "project_id": project_id,
            "private_key_id": random_string(40, string.hexdigits).lower(),
            "client_email": f"{project_id}@{project_id}.iam.gserviceaccount.com",
            "client_id": str(random.randint(100000000000000000000, 999999999999999999999)),
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }, separators=(',', ':')),
        "GCP_STORAGE_BUCKET": f"{project_id}-storage",
        "GCP_REGION": random.choice(["us-central1", "us-east1", "europe-west1", "asia-east1"]),
        "GCP_CREDENTIALS_FILE": f"/app/config/{project_id}-credentials.json"
    }