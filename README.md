

<h1 align="center">Heimdall – The Gatekeeper of Deceptive Credentials</h1>
<p align="center"><i>Environment files crafted for curious attackers</i></p>

---

## What is Heimdall ?

**Heimdall** is a powerful CLI **honeypot** that generates **realistic-looking `.env` files** for a wide range of cloud services, databases, and APIs.  
It’s built for red teams, honeypots setup, CTFs, and anyone needing fake but plausible credentials.

> <i>In Norse mythology, **Heimdall** guards the Bifröst — the rainbow bridge between worlds.</i>  
> <i>Just like the god, this tool stands between attackers and real secrets, showing them only what you want them to see.</i>

---

## Features

- Fake `.env` files with **valid patterns and naming**
- Designed for **deception**, **red teaming**, and **training environments**
- Supports dozens of services: AWS, Firebase, MongoDB, Stripe, Supabase, etc.
- Easy to extend — add your own templates
- Outputs a single `.env` or multiple files, ready to deploy

---

## Examples

Generate AWS credentials in JSON format:

- `python3 heimdall.py -t aws -f json`

Generate multiple MySQL credential files:

- `python3 heimdall.py -t mysql -c 5`

Generate all credential types at once:

- `python3 heimdall.py -t all -d ./credentials`

List all available credential types:

- `python3 heimdall.py -t list`

Generate a complete environment file with at least 30 variables:

- `python3 heimdall.py -t dotenv -m 30`

---

## Available Credential Types

| Type | Description |
|------|-------------|
| `api` | Various API keys for different services |
| `aws` | Amazon Web Services credentials |
| `azure` | Microsoft Azure credentials |
| `dotenv` | Complete .env file with multiple credential types (50+ variables) |
| `gcp` | Google Cloud Platform credentials |
| `github` | GitHub access tokens and account info |
| `jwt` | JSON Web Token credentials |
| `mongo` | MongoDB database connection details |
| `mysql` | MySQL database connection details |
| `oauth` | OAuth2 authentication details |
| `payment` | Payment processor credentials |
| `postgres` | PostgreSQL database connection details |
| `redis` | Redis database connection details |
| `s3` | S3-compatible storage credentials |
| `smtp` | Email/SMTP server configuration |
| `ssh` | SSH key pairs for server access |

---

## Contribute

Heimdall is designed to be modular and extensible. You can easily contribute new services by defining their environment variables and realistic patterns. If you wish to incorporate a new service into the project, you can develop the necessary functionality and submit a pull request.
  
  
> <i>Let them steal what you created.</i>
