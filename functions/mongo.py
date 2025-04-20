"""
MongoDB credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_ip, random_domain

def generate_mongo():
    """Generate fake MongoDB credentials."""
    username = random_string(random.randint(6, 10))
    password = random_string(random.randint(10, 16), string.ascii_letters + string.digits + "!@#$")
    host = random.choice(["localhost", random_ip(), random_domain()])
    port = random.choice(["27017", "27018", "27019"])
    db_name = random.choice(["app", "production", "main", "data", "analytics", "userdb"])
    
    # Different connection string formats
    format_type = random.choice(["standard", "srv", "replica"])
    
    if format_type == "standard":
        uri = f"mongodb://{username}:{password}@{host}:{port}/{db_name}"
    elif format_type == "srv":
        uri = f"mongodb+srv://{username}:{password}@{host}/{db_name}"
    else:  # replica set
        replica_name = random.choice(["rs0", "replicaSet", "cluster0"])
        hosts = [random_domain() for _ in range(3)]
        uri = f"mongodb://{username}:{password}@{','.join(hosts)}/{db_name}?replicaSet={replica_name}"
    
    return {
        "MONGO_URI": uri,
        "MONGO_USER": username,
        "MONGO_PASSWORD": password,
        "MONGO_DB": db_name,
        "MONGO_HOST": host,
        "MONGO_PORT": port,
        "MONGO_AUTH_SOURCE": random.choice(["admin", db_name]),
        "MONGO_AUTH_MECHANISM": random.choice(["SCRAM-SHA-1", "SCRAM-SHA-256"])
    }
