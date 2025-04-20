"""
API keys generator for Heimdall.
"""

import random
import string
from functions.utils import random_string

def generate_api_keys():
    """Generate a set of API keys for different services."""
    # Choose 2-3 API services
    api_services = [
        "stripe", "twilio", "sendgrid", "mailchimp", "openai", "slack", 
        "discord", "segment", "sentry", "algolia", "cloudflare", "datadog",
        "digitalocean", "firebase", "hubspot", "intercom", "mailgun", "nexmo",
        "pusher", "pubnub", "clearbit", "chargebee", "contentful", "fastly"
    ]
    
    selected_services = random.sample(api_services, random.randint(2, 3))
    result = {}
    
    prefixes = {
        "stripe": "sk_test_",
        "twilio": "SK",
        "sendgrid": "SG.",
        "mailchimp": "mc-",
        "openai": "sk-",
        "slack": "xoxp-",
        "discord": "ODM",
        "segment": "seg_",
        "sentry": "sentry_",
        "algolia": "alg_",
        "cloudflare": "cf_",
        "datadog": "dd_",
        "digitalocean": "dop_v1_",
        "firebase": "fir_",
        "hubspot": "hs_",
        "intercom": "ic_",
        "mailgun": "key-",
        "nexmo": "nexmo_",
        "pusher": "pusher_",
        "pubnub": "pub_",
        "clearbit": "sk_",
        "chargebee": "live_",
        "contentful": "cftoken_",
        "fastly": "fastly_"
    }
    
    for service in selected_services:
        prefix = prefixes.get(service, "")
        
        # Generate the API key with appropriate prefix and length
        key_length = random.randint(24, 48)
        result[f"{service.upper()}_API_KEY"] = prefix + random_string(key_length - len(prefix))
        
        # Add a corresponding API secret when appropriate
        if service not in ["sendgrid", "mailchimp"]:
            result[f"{service.upper()}_API_SECRET"] = random_string(random.randint(24, 40))
        
        # Add extra service-specific credentials
        if service == "stripe":
            result["STRIPE_PUBLISHABLE_KEY"] = "pk_test_" + random_string(24)
            result["STRIPE_WEBHOOK_SECRET"] = "whsec_" + random_string(24)
        elif service == "twilio":
            result["TWILIO_ACCOUNT_SID"] = "AC" + random_string(32, string.digits)
            result["TWILIO_AUTH_TOKEN"] = random_string(32)
            result["TWILIO_PHONE_NUMBER"] = f"+1{random.randint(2000000000, 9999999999)}"
    
    return result