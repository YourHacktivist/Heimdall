"""
Payment processor credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string

def generate_payment():
    """Generate fake payment processor credentials."""
    processor = random.choice(["stripe", "paypal", "braintree", "adyen", "square"])
    
    if processor == "stripe":
        return {
            "STRIPE_SECRET_KEY": "sk_" + random.choice(["test", "live"]) + "_" + random_string(24),
            "STRIPE_PUBLISHABLE_KEY": "pk_" + random.choice(["test", "live"]) + "_" + random_string(24),
            "STRIPE_WEBHOOK_SECRET": "whsec_" + random_string(24),
            "STRIPE_ACCOUNT_ID": "acct_" + random_string(16),
            "STRIPE_API_VERSION": random.choice(["2022-11-15", "2023-08-16", "2024-01-01"]),
            "STRIPE_ENDPOINT_SECRET": "whsec_" + random_string(24)
        }
    elif processor == "paypal":
        return {
            "PAYPAL_CLIENT_ID": random_string(24),
            "PAYPAL_CLIENT_SECRET": random_string(40),
            "PAYPAL_MODE": random.choice(["sandbox", "live"]),
            "PAYPAL_WEBHOOK_ID": random_string(36, string.hexdigits).lower(),
            "PAYPAL_API_URL": f"https://api-m.{random.choice(['sandbox.paypal.com', 'paypal.com'])}",
            "PAYPAL_MERCHANT_ID": random_string(13, string.digits)
        }
    elif processor == "braintree":
        return {
            "BRAINTREE_MERCHANT_ID": random_string(8),
            "BRAINTREE_PUBLIC_KEY": random_string(16),
            "BRAINTREE_PRIVATE_KEY": random_string(32),
            "BRAINTREE_ENVIRONMENT": random.choice(["Sandbox", "Production"]),
            "BRAINTREE_MERCHANT_ACCOUNT_ID": random_string(16),
            "BRAINTREE_TOKENIZATION_KEY": random_string(32)
        }
    elif processor == "adyen":
        return {
            "ADYEN_MERCHANT_ACCOUNT": random_string(12),
            "ADYEN_API_KEY": "AQE" + random_string(36),
            "ADYEN_CLIENT_KEY": random_string(24),
            "ADYEN_HMAC_KEY": random_string(32),
            "ADYEN_LIVE_URL_PREFIX": random_string(8).lower(),
            "ADYEN_ENVIRONMENT": random.choice(["test", "live"])
        }
    else:  # square
        return {
            "SQUARE_ACCESS_TOKEN": random.choice(["EAAAEBmQ", "EAAAEP"]) + random_string(56),
            "SQUARE_LOCATION_ID": random_string(12),
            "SQUARE_APPLICATION_ID": "sq0" + random.choice(["idp", "app"]) + "-" + random_string(16),
            "SQUARE_APPLICATION_SECRET": "sq0" + random.choice(["csp", "sap"]) + "-" + random_string(32),
            "SQUARE_ENVIRONMENT": random.choice(["sandbox", "production"])
        }
