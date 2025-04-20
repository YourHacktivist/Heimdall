"""
Amazon Web Services credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_aws():
    """Generate fake AWS credentials."""
    return {
        "AWS_ACCESS_KEY_ID": "AKIA" + random_string(16, string.ascii_uppercase + string.digits),
        "AWS_SECRET_ACCESS_KEY": random_string(40),
        "AWS_REGION": random.choice(["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1", "sa-east-1"]),
        "AWS_S3_BUCKET": f"{random_string(8).lower()}-{random.choice(['data', 'assets', 'media', 'backup', 'storage'])}-{random.randint(100, 999)}",
        "AWS_CLOUDFRONT_DISTRIBUTION_ID": "E" + random_string(13, string.ascii_uppercase + string.digits),
        "AWS_LAMBDA_FUNCTION": f"{random.choice(['app', 'api', 'worker', 'cron'])}-{random.choice(['prod', 'staging', 'dev'])}-{random_string(6).lower()}",
        "AWS_EC2_INSTANCE_ID": "i-" + random_string(17, string.ascii_lowercase + string.digits)
    }