"""
S3-compatible storage credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_s3():
    """Generate fake S3-compatible storage credentials."""
    provider = random.choice(["aws", "minio", "digitalocean", "wasabi", "backblaze"])
    
    bucket = f"{random_string(8).lower()}-{random.choice(['media', 'assets', 'static', 'uploads', 'backups'])}"
    
    if provider == "aws":
        region = random.choice(["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"])
        return {
            "S3_ACCESS_KEY": "AKIA" + random_string(16, string.ascii_uppercase + string.digits),
            "S3_SECRET_KEY": random_string(40),
            "S3_BUCKET": bucket,
            "S3_REGION": region,
            "S3_ENDPOINT": f"https://s3.{region}.amazonaws.com",
            "S3_URL": f"https://{bucket}.s3.{region}.amazonaws.com"
        }
    elif provider == "minio":
        return {
            "S3_ACCESS_KEY": random_string(20),
            "S3_SECRET_KEY": random_string(40),
            "S3_BUCKET": bucket,
            "S3_REGION": "us-east-1",
            "S3_ENDPOINT": f"https://minio.{random_domain()}",
            "S3_USE_PATH_STYLE": "true"
        }
    elif provider == "digitalocean":
        region = random.choice(["nyc3", "sfo2", "sgp1", "fra1"])
        return {
            "S3_ACCESS_KEY": random_string(20),
            "S3_SECRET_KEY": random_string(40),
            "S3_BUCKET": bucket,
            "S3_REGION": region,
            "S3_ENDPOINT": f"https://{region}.digitaloceanspaces.com",
            "S3_URL": f"https://{bucket}.{region}.digitaloceanspaces.com"
        }
    elif provider == "wasabi":
        region = random.choice(["us-east-1", "eu-central-1", "ap-northeast-1"])
        return {
            "S3_ACCESS_KEY": random_string(20),
            "S3_SECRET_KEY": random_string(40),
            "S3_BUCKET": bucket,
            "S3_REGION": region,
            "S3_ENDPOINT": f"https://s3.{region}.wasabisys.com",
            "S3_URL": f"https://{bucket}.s3.{region}.wasabisys.com"
        }
    else:  # backblaze
        return {
            "S3_ACCESS_KEY": random_string(12, string.digits) + random_string(8),
            "S3_SECRET_KEY": random_string(40),
            "S3_BUCKET": bucket,
            "S3_REGION": "us-west-002",
            "S3_ENDPOINT": "https://s3.us-west-002.backblazeb2.com",
            "S3_URL": f"https://f002.backblazeb2.com/file/{bucket}"
        }
