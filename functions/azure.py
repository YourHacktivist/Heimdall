"""
Microsoft Azure credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string

def generate_azure():
    """Generate fake Azure credentials."""
    tenant_id = random_string(36, string.hexdigits).lower()
    subscription_id = random_string(36, string.hexdigits).lower()
    return {
        "AZURE_TENANT_ID": tenant_id,
        "AZURE_SUBSCRIPTION_ID": subscription_id,
        "AZURE_CLIENT_ID": random_string(36, string.hexdigits).lower(),
        "AZURE_CLIENT_SECRET": random_string(40),
        "AZURE_RESOURCE_GROUP": f"rg-{random.choice(['app', 'web', 'api', 'data'])}-{random.choice(['prod', 'staging', 'dev'])}",
        "AZURE_STORAGE_ACCOUNT": f"storage{random_string(8).lower()}",
        "AZURE_STORAGE_CONTAINER": random.choice(["media", "assets", "files", "data", "backup"]),
        "AZURE_REGION": random.choice(["eastus", "westus2", "westeurope", "southeastasia"])
    }
