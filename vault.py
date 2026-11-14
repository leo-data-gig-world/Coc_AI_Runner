"""Load API keys from Windows Credential Manager into environment variables.

Keys are never kept in files. Store each one once (it asks for the value, hidden):

    python -m keyring set leo-secrets OPENROUTER_API_KEY

Real environment variables always win, so in production a secret manager can
inject the same names and this file does nothing.
"""
import os

SERVICE = "leo-secrets"


def load(*names: str) -> None:
    try:
        import keyring
    except ImportError:
        print("vault: `pip install keyring` to load API keys from Windows Credential Manager")
        return
    for name in names:
        if not os.environ.get(name):
            value = keyring.get_password(SERVICE, name)
            if value:
                os.environ[name] = value
