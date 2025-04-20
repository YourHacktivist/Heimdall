"""
SMTP credential generator for Heimdall.
"""

import random
import string
from functions.utils import random_string, random_domain

def generate_smtp():
    """Generate fake SMTP credentials."""
    provider = random.choice(["gmail", "sendgrid", "mailgun", "amazon_ses", "mailchimp"])
    
    if provider == "gmail":
        email = f"{random_string(8).lower()}@gmail.com"
        return {
            "SMTP_HOST": "smtp.gmail.com",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": email,
            "SMTP_PASSWORD": random_string(16, string.ascii_letters + string.digits + "!@#$%^&*"),
            "SMTP_SECURE": "true",
            "SMTP_FROM_EMAIL": email,
            "SMTP_FROM_NAME": f"{random_string(6).capitalize()} {random_string(8).capitalize()}"
        }
    elif provider == "sendgrid":
        return {
            "SMTP_HOST": "smtp.sendgrid.net",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": "apikey",
            "SMTP_PASSWORD": "SG." + random_string(66),
            "SMTP_SECURE": "false",
            "SMTP_FROM_EMAIL": f"{random_string(8).lower()}@{random_domain()}",
            "SMTP_FROM_NAME": random.choice(["Support", "Info", "No-Reply", "Admin"]) + f" {random_string(6).capitalize()}"
        }
    elif provider == "mailgun":
        return {
            "SMTP_HOST": "smtp.mailgun.org",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": f"postmaster@{random_domain()}",
            "SMTP_PASSWORD": random_string(32),
            "SMTP_SECURE": "true",
            "SMTP_DOMAIN": random_domain(),
            "SMTP_API_KEY": "key-" + random_string(32)
        }
    elif provider == "amazon_ses":
        return {
            "SMTP_HOST": f"email-smtp.{random.choice(['us-east-1', 'us-west-2', 'eu-west-1'])}.amazonaws.com",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": "AKIA" + random_string(16, string.ascii_uppercase + string.digits),
            "SMTP_PASSWORD": random_string(40),
            "SMTP_SECURE": "true",
            "SMTP_REGION": random.choice(["us-east-1", "us-west-2", "eu-west-1"]),
            "SMTP_FROM_EMAIL": f"no-reply@{random_domain()}"
        }
    else:  # mailchimp
        return {
            "SMTP_HOST": "smtp.mandrillapp.com",
            "SMTP_PORT": "587",
            "SMTP_USERNAME": f"{random_string(8).lower()}@{random_domain()}",
            "SMTP_PASSWORD": random_string(20),
            "SMTP_SECURE": "true",
            "SMTP_API_KEY": "md-" + random_string(32),
            "SMTP_FROM_DOMAIN": random_domain()
        }
