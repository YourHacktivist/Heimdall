"""
MySQL credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_ip, random_domain

def generate_mysql():
    """Generate fake MySQL credentials."""
    username = random.choice(["root", "admin", "dbuser", "app_user", random_string(8).lower()])
    password = random_string(random.randint(12, 20), string.ascii_letters + string.digits + "!@#$%^&*")
    host = random.choice(["localhost", random_ip(), random_domain()])
    port = "3306"
    db_name = random.choice(["mysql", "app_db", "production", "main", random_string(8).lower()])
    
    # Different connection string formats
    format_type = random.choice(["standard", "params"])
    
    if format_type == "standard":
        url = f"mysql://{username}:{password}@{host}:{port}/{db_name}"
    else:  # with parameters
        params = ["charset=utf8mb4", "parseTime=True", "loc=Local"]
        url = f"mysql://{username}:{password}@{host}:{port}/{db_name}?{'&'.join(params)}"
    
    return {
        "MYSQL_URL": url,
        "MYSQL_USER": username,
        "MYSQL_PASSWORD": password,
        "MYSQL_DATABASE": db_name,
        "MYSQL_HOST": host,
        "MYSQL_PORT": port,
        "MYSQL_CHARSET": "utf8mb4",
        "MYSQL_CONNECTION_LIMIT": str(random.randint(5, 20))
    }
