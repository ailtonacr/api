from fastapi import Request, HTTPException
from starlette.responses import RedirectResponse
from .token_manager import TokenManager
from .session_manager import SessionManager


class AuthHandler:
    def __init__(self):
        self.token_manager = TokenManager()

    async def login_redirect(self, request: Request, redirect_url: str):
        auth_url = self.token_manager.get_authorization_url()
        request.session["redirect_url"] = redirect_url
        return RedirectResponse(auth_url)

    async def callback_redirect(self, request: Request):
        code = request.query_params.get("code")
        if not code:
            raise HTTPException(status_code=400, detail="Authorization code not found")

        token, expires_at = self.token_manager.acquire_token_from_code(code)
        SessionManager.store_token(request, token, expires_at)
        redirect_url = request.session.pop("redirect_url", "/")
        return RedirectResponse(url=redirect_url)
