"""
Redis credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_ip, random_domain

def generate_redis():
    """Generate fake Redis credentials."""
    password = random_string(random.randint(12, 20), string.ascii_letters + string.digits)
    host = random.choice(["localhost", random_ip(), random_domain()])
    port = "6379"
    db_number = str(random.randint(0, 15))
    
    # Different connection string formats
    format_type = random.choice(["standard", "sentinel", "cluster"])
    
    if format_type == "standard":
        url = f"redis://{password}@{host}:{port}/{db_number}"
    elif format_type == "sentinel":
        sentinel_name = random.choice(["mymaster", "redis-ha", "main"])
        url = f"redis+sentinel://{password}@{host}:{port}/{db_number}?sentinel={sentinel_name}"
    else:  # cluster
        nodes = [f"{random_ip()}:6379" for _ in range(3)]
        url = f"redis+cluster://{password}@{','.join(nodes)}"
    
    return {
        "REDIS_URL": url,
        "REDIS_HOST": host,
        "REDIS_PORT": port,
        "REDIS_PASSWORD": password,
        "REDIS_DB": db_number,
        "REDIS_PREFIX": random.choice(["app:", "cache:", "session:", ""]),
        "REDIS_SSL": random.choice(["true", "false"])
    }
