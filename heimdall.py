#!/usr/bin/env python3

import random
import string
import argparse
import datetime
import json
import os
import sys
from pathlib import Path
import hashlib
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

from functions import (
    generate_aws, generate_gcp, generate_azure, generate_github,
    generate_mongo, generate_postgres, generate_mysql, generate_redis,
    generate_api_keys, generate_jwt, generate_oauth, generate_payment,
    generate_smtp, generate_s3, generate_ssh, generate_dotenv
)
# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Version information
VERSION = "1.0.0"

# Initialize Rich console
console = Console()

# Create banner using Rich
def get_banner():
    title = Text("HEIMDALL - The Gatekeeper of Deceptive Credentials", style="bold cyan")
    subtitle = Text("\nEnvironments files crafted for curious attackers", style="cyan")
    version_info = Text(f"\nVersion {VERSION}", style="dim")
    
    content = Text.assemble(title, "\n", subtitle, version_info)
    panel = Panel(
        content,
        box=box.ROUNDED,
        border_style="cyan",
        padding=(1, 2),
    )
    
    return panel

# Banner for CLI as a function
def print_banner():
    console.print(get_banner())

def get_banner_text():
    """Return a plain text version of the banner for CLI help."""
    return """
HEIMDALL - The Gatekeeper of Deceptive Credentials

Environments files crafted for curious attackers

Version {}
""".format(VERSION)

BANNER = get_banner_text()

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

def format_env(creds_dict):
    """Format credentials as environment variables."""
    lines = [f"{k}={v}" for k, v in creds_dict.items()]
    return "\n".join(lines)

def format_txt(creds_dict):
    """Format credentials as plain text."""
    lines = [f"{k}: {v}" for k, v in creds_dict.items()]
    return "\n".join(lines)

def format_json(creds_dict):
    """Format credentials as JSON."""
    return json.dumps(creds_dict, indent=4)

def format_yaml(creds_dict):
    """Format credentials as YAML with proper indentation."""
    try:
        import yaml
        return yaml.dump(creds_dict, default_flow_style=False, sort_keys=False)
    except ImportError:
        lines = []
        for k, v in creds_dict.items():
            if isinstance(v, str):
                v = v.replace("'", "''")
                if "\n" in v:
                    lines.append(f"{k}: |\n" + "\n".join(f"  {line}" for line in v.split("\n")))
                else:
                    lines.append(f"{k}: '{v}'")
            else:
                lines.append(f"{k}: {v}")
        return "\n".join(lines)

def get_fake_timestamp():
    """Generate a realistic fake timestamp within the last 180 days."""
    today = datetime.date.today()
    delta = datetime.timedelta(days=random.randint(0, 180))
    fake_date = today - delta
    
    # Add time component
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    return fake_date.strftime(f"%Y-%m-%d %H:%M:%S").replace(" ", "T") + "Z"

def get_header(file_format):
    """Generate a realistic looking file header."""
    comment_styles = {
        "env": "#",
        "txt": "#",
        "json": "//",
        "yaml": "#"
    }
    
    comment = comment_styles.get(file_format, "#")
    timestamp = get_fake_timestamp()
    commit_msg = random.choice([
        "Update credentials for production",
        "Add new API keys",
        "Rotate keys for security",
        "Security update",
        "Update access credentials",
        "Emergency credential rotation",
        "New deployment keys",
        "Project migration keys"
    ])
    
    lines = [
        f"{comment} {commit_msg}",
        f"{comment} Last updated: {timestamp}",
        f"{comment} IMPORTANT: DO NOT SHARE THESE CREDENTIALS",
        ""
    ]
    
    return "\n".join(lines)

TYPES = {
    "aws": generate_aws,
    "gcp": generate_gcp,
    "azure": generate_azure,
    "github": generate_github,
    "mongo": generate_mongo,
    "postgres": generate_postgres,
    "mysql": generate_mysql,
    "redis": generate_redis,
    "api": generate_api_keys,
    "jwt": generate_jwt,
    "oauth": generate_oauth,
    "payment": generate_payment,
    "smtp": generate_smtp,
    "s3": generate_s3,
    "ssh": generate_ssh,
    "dotenv": generate_dotenv
}

FORMATS = {
    "env": format_env,
    "txt": format_txt,
    "json": format_json,
    "yaml": format_yaml
}

def print_color(text, color):
    """Print text with color."""
    print(f"{color}{text}{Colors.ENDC}")

def list_types():
    """Print available credential types and their descriptions."""
    print("\nAvailable credential types:")
    print("-------------------------")
    descriptions = {
        "aws": "Amazon Web Services credentials",
        "gcp": "Google Cloud Platform credentials",
        "azure": "Microsoft Azure credentials",
        "github": "GitHub access tokens and account info",
        "mongo": "MongoDB database connection details",
        "postgres": "PostgreSQL database connection details",
        "mysql": "MySQL database connection details",
        "redis": "Redis database connection details",
        "api": "Various API keys for different services",
        "jwt": "JSON Web Token credentials",
        "oauth": "OAuth2 authentication details",
        "payment": "Payment processor credentials",
        "smtp": "Email/SMTP server configuration",
        "s3": "S3-compatible storage credentials",
        "ssh": "SSH key pairs for server access",
        "dotenv": "Complete .env file with multiple credential types (50+ variables)"
    }
    
    for t in sorted(TYPES.keys()):
        print(f"  {Colors.CYAN}{t:<10}{Colors.ENDC} - {descriptions.get(t, 'No description')}")

def main():
    """Main function to handle command line arguments and generate credentials."""
    parser = argparse.ArgumentParser(
        description=get_banner_text(),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    
    parser.add_argument(
        "-t", "--type", 
        choices=list(TYPES.keys()) + ["all", "list"], 
        default="dotenv",
        help="Type of credential to generate (default: dotenv, use 'list' to see options)"
    )
    
    parser.add_argument(
        "-f", "--format", 
        choices=FORMATS.keys(), 
        default="env", 
        help="Output format (default: env)"
    )
    
    parser.add_argument(
        "-o", "--output", 
        help="Output filename (default: auto-generated)"
    )
    
    parser.add_argument(
        "-d", "--directory", 
        help="Directory to store generated files (default: current directory)"
    )
    
    parser.add_argument(
        "-c", "--count", 
        type=int, 
        default=1, 
        help="Number of files to generate (default: 1)"
    )
    
    parser.add_argument(
        "-m", "--min-vars",
        type=int,
        default=0,
        help="Minimum number of variables to include in each file (default: depends on type)"
    )
    
    parser.add_argument(
        "-q", "--quiet", 
        action="store_true", 
        help="Suppress output messages"
    )
    
    parser.add_argument(
        "-v", "--version",
        action="version",
        version=f"Heimdall v{VERSION}",
        help="Show version information and exit"
    )
    
    args = parser.parse_args()
    
    if not args.quiet:
        print_banner()

    if args.type == "list":
        list_types()
        sys.exit(0)
    
    output_dir = args.directory or "."
    if args.directory:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

    cred_types = list(TYPES.keys()) if args.type == "all" else [args.type]
    
    # Generate the specified number of files
    for i in range(args.count):
        for cred_type in cred_types:
            # Generate credentials
            creds = TYPES[cred_type]()
            
            # Ensure minimum number of variables if specified
            if args.min_vars > 0 and len(creds) < args.min_vars:
                # Add random variables until we reach the minimum
                extra_needed = args.min_vars - len(creds)
                for j in range(extra_needed):
                    var_name = f"EXTRA_VAR_{j+1}"
                    creds[var_name] = random_string(random.randint(16, 32))
            
            # Format content according to chosen format
            content = FORMATS[args.format](creds)
            
            # Generate header
            header = get_header(args.format)
            
            # Determine filename
            if args.output:
                filename = args.output
            elif cred_type == "dotenv":
                # For dotenv, use .env as the name
                random_suffix = f"_{i+1}" if args.count > 1 else ""
                filename = f".env{random_suffix}"
            elif args.count > 1 or len(cred_types) > 1:
                # Auto-generate a unique filename when creating multiple files
                random_suffix = f"_{i+1}"
                filename = f"{cred_type}{random_suffix}.{args.format}"
            else:
                filename = f"{cred_type}.{args.format}"
                
            filepath = os.path.join(output_dir, filename)
            
            # Write to file
            with open(filepath, "w") as f:
                f.write(header + "\n" + content + "\n")
            
            if not args.quiet:
                print(f"\n[ {Colors.GREEN}>{Colors.ENDC} ] Fake {Colors.CYAN}{cred_type.upper()}{Colors.ENDC} credentials saved to: {Colors.BOLD}{filepath}{Colors.ENDC}\n")
                print(f"[ {Colors.BLUE}?{Colors.ENDC} ] Contains {Colors.BOLD}{len(creds)}{Colors.ENDC} environment variables\n")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n[{Colors.WARNING}!{Colors.ENDC}] Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n[{Colors.FAIL} ! {Colors.ENDC}] Error: {e}")
        sys.exit(1)