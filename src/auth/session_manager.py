from datetime import datetime, timedelta
from fastapi import Request


class SessionManager:
    @staticmethod
    def store_token(request: Request, token: str, expires_at: datetime):
        request.session["access_token"] = token
        request.session["expires_at"] = expires_at.isoformat()

    @staticmethod
    def get_current_user(request: Request):
        token = request.session.get("access_token")
        expires_at_str = request.session.get("expires_at")
        if not token or not expires_at_str:
            return None

        expires_at = datetime.fromisoformat(expires_at_str)
        if datetime.utcnow() >= expires_at:
            request.session.pop("access_token", None)
            request.session.pop("expires_at", None)
            return None

        new_expires_at = datetime.utcnow() + timedelta(seconds=600)
        request.session["expires_at"] = new_expires_at.isoformat()

        return token
