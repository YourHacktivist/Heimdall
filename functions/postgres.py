"""
PostgreSQL credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_ip, random_domain

def generate_postgres():
    """Generate fake PostgreSQL credentials."""
    username = random.choice(["postgres", "admin", "dbuser", "app_user", random_string(8).lower()])
    password = random_string(random.randint(12, 20), string.ascii_letters + string.digits + "!@#$%^&*")
    host = random.choice(["localhost", random_ip(), random_domain()])
    port = "5432"
    db_name = random.choice(["postgres", "app_db", "production", "main", random_string(8).lower()])
    
    # Different connection string formats
    format_type = random.choice(["standard", "params"])
    
    if format_type == "standard":
        url = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"
    else:  # with parameters
        params = ["sslmode=require", "application_name=myapp", f"connect_timeout={random.randint(10, 30)}"]
        url = f"postgresql://{username}:{password}@{host}:{port}/{db_name}?{'&'.join(params)}"
    
    return {
        "POSTGRES_URL": url,
        "POSTGRES_USER": username,
        "POSTGRES_PASSWORD": password,
        "POSTGRES_DB": db_name,
        "POSTGRES_HOST": host,
        "POSTGRES_PORT": port,
        "POSTGRES_SCHEMA": random.choice(["public", "app", "v1", "main"]),
        "POSTGRES_SSL": random.choice(["true", "false"])
    }
