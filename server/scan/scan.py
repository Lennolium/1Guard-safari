#!/usr/bin/env python3

"""
scan.py: TODO: Headline...

TODO: Description...
"""

# Header.
__author__ = "Lennart Haack"
__email__ = "lennart-haack@mail.de"
__license__ = "GNU GPLv3"
__version__ = "0.0.1"
__build__ = "2023.1"
__date__ = "2023-11-07"
__status__ = "Prototype"

# Imports.
import whois


def get_whois_info(domain):
    try:
        domain_info = whois.query(domain)
        return domain_info
    except Exception as e:
        print(f"Error: {e}")
        return None


# TODO: Implement the user score function.
def get_user_score_trustpilot(domain):
    return 3


if __name__ == "__main__":
    # Beispiel-Nutzung
    website_domain = 'chicladdy.com'
    whois_info = get_whois_info(website_domain)

    if whois_info:
        print(whois_info.__dict__)
    else:
        print("WHOIS-Informationen nicht verfügbar.")
