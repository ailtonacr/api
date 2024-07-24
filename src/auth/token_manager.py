from msal import ConfidentialClientApplication
from datetime import datetime, timedelta
from fastapi import HTTPException
import os


class TokenManager:
    def __init__(self):
        self.CLIENT_ID = os.getenv("CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("CLIENT_SECRET")
        self.TENANT_ID = os.getenv("TENANT_ID")
        self.AUTHORITY = f"https://login.microsoftonline.com/{self.TENANT_ID}"
        self.REDIRECT_URI = os.getenv("REDIRECT_URI")
        self.SCOPE = [os.getenv("SCOPE")]

        self.msal_app = ConfidentialClientApplication(
            self.CLIENT_ID, authority=self.AUTHORITY, client_credential=self.CLIENT_SECRET
        )

    def get_authorization_url(self):
        return self.msal_app.get_authorization_request_url(
            self.SCOPE, redirect_uri=self.REDIRECT_URI
        )

    def acquire_token_from_code(self, code: str):
        result = self.msal_app.acquire_token_by_authorization_code(
            code, scopes=self.SCOPE, redirect_uri=self.REDIRECT_URI
        )
        if "access_token" in result:
            expires_in = result.get("expires_in", 600)
            expires_at = datetime.utcnow() + timedelta(seconds=expires_in)
            return result["access_token"], expires_at
        else:
            error_description = result.get("error_description", "Unknown error")
            raise HTTPException(status_code=400, detail=f"Token acquisition failed: {error_description}")
