"""
Complete .env file generator for Heimdall.
"""

import random
import datetime
import importlib

def generate_dotenv():
    """Generate a comprehensive .env file with many environment variables."""
    result = {}
    
    # Basic environment configuration
    result["NODE_ENV"] = random.choice(["production", "staging", "development"])
    result["PORT"] = str(random.randint(3000, 8999))
    result["HOST"] = random.choice(["0.0.0.0", "localhost", "127.0.0.1"])
    result["LOG_LEVEL"] = random.choice(["debug", "info", "warn", "error"])
    result["DEBUG"] = random.choice(["true", "false"])
    result["TZ"] = random.choice(["UTC", "America/New_York", "Europe/London", "Asia/Tokyo"])
    
    # Application configuration
    from functions.utils import random_string, random_domain
    result["APP_NAME"] = random_string(random.randint(5, 10))
    result["APP_URL"] = f"https://{random_domain()}"
    result["APP_VERSION"] = f"{random.randint(1, 5)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    result["APP_ENV"] = result["NODE_ENV"]
    result["APP_KEY"] = random_string(32)
    result["APP_DEBUG"] = result["DEBUG"]
    
    # Select 4-7 credential types to include
    cred_modules = [
        "aws", "gcp", "azure", "github", "mongo", "postgres", 
        "mysql", "redis", "api_keys", "jwt", "oauth", "payment",
        "smtp", "s3", "ssh"
    ]
    
    selected_modules = random.sample(cred_modules, random.randint(4, 7))
    
    # Include selected credential types
    for module_name in selected_modules:
        module = importlib.import_module(f"functions.{module_name}")
        generator_function = getattr(module, f"generate_{module_name}")
        creds = generator_function()
        result.update(creds)
    
    # CORS settings
    result["CORS_ORIGIN"] = random.choice(["*", f"https://{random_domain()}"]) 
    result["CORS_METHODS"] = "GET,POST,PUT,DELETE,OPTIONS"
    result["CORS_CREDENTIALS"] = random.choice(["true", "false"])
    
    # Security settings
    result["COOKIE_SECRET"] = random_string(32)
    result["SESSION_SECRET"] = random_string(32)
    result["ENCRYPTION_KEY"] = random_string(32)
    
    # Miscellaneous configs
    result["SENTRY_DSN"] = f"https://{random_string(16)}@{random.randint(1000000, 9999999)}.ingest.sentry.io/{random.randint(10000, 99999)}"
    result["ANALYTICS_ID"] = f"UA-{random.randint(10000000, 99999999)}-{random.randint(1, 9)}"
    
    # Add timestamps and version info
    result["BUILD_TIMESTAMP"] = str(int(datetime.datetime.now().timestamp()))
    result["DEPLOY_DATE"] = datetime.datetime.now().strftime("%Y-%m-%d")
    
    return result
