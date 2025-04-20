"""
Utility functions for Heimdall credential generators.
"""

import random
import string

def random_string(length, chars=string.ascii_letters + string.digits):
    """Generate a random string of specified length using given character set."""
    return ''.join(random.choices(chars, k=length))

def random_ip():
    """Generate a random IP address."""
    return f"{random.randint(1, 254)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"

def random_domain():
    """Generate a random domain name."""
    tlds = ['com', 'net', 'org', 'io', 'cloud', 'dev', 'tech']
    return f"{random_string(random.randint(5, 10)).lower()}.{random.choice(tlds)}"