"""
SSH credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_ssh():
    """Generate fake SSH credentials."""
    key_types = ["rsa", "ed25519", "ecdsa"]
    key_type = random.choice(key_types)
    
    # Fake private key content
    private_key = f"""-----BEGIN {key_type.upper()} PRIVATE KEY-----
{random_string(400)}
{random_string(400)}
{random_string(400)}
{random_string(64)}=
-----END {key_type.upper()} PRIVATE KEY-----"""
    
    # Fake public key content
    public_key = f"{key_type} {random_string(372)} user@{random_domain()}"
    
    return {
        "SSH_PRIVATE_KEY": private_key,
        "SSH_PUBLIC_KEY": public_key,
        "SSH_HOST": random_domain(),
        "SSH_PORT": random.choice(["22", "2222", "22022"]),
        "SSH_USER": random.choice(["root", "admin", "ubuntu", "ec2-user", "deploy"]),
        "SSH_PASSPHRASE": random_string(random.randint(12, 20), string.ascii_letters + string.digits + "!@#$%^&*"),
        "SSH_KEY_PATH": f"/home/user/.ssh/id_{key_type}"
    }
