from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import JSONResponse
from dotenv import load_dotenv
import os
from auth import AuthHandler, SessionManager
from database import DBOperations

load_dotenv()

app = FastAPI(docs_url=None, redoc_url=None, favicon=None)
app.add_middleware(SessionMiddleware, secret_key=os.getenv("SESSION_SECRET_KEY"), max_age=None)

auth_handler = AuthHandler()
db_operations = DBOperations()


def get_current_user(request: Request):
    token = SessionManager.get_current_user(request)
    if token is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return token


@app.get("/health")
def check():
    return {"message": "Tô on!"}


@app.get("/login")
async def login(request: Request):
    return await auth_handler.login_redirect(request, "/")


@app.get("/callback", include_in_schema=False)
async def callback(request: Request):
    return await auth_handler.callback_redirect(request)


@app.post("/add")
async def add_guest(request: Request, user=Depends(get_current_user)):
    data = await request.json()
    name = data.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")
    result = db_operations.add_name(name)
    return JSONResponse(content=result)


@app.delete("/remove")
async def remove_guest(request: Request, user=Depends(get_current_user)):
    data = await request.json()
    name = data.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")
    result = db_operations.remove_name(name)
    return JSONResponse(content=result)


@app.get("/list")
async def show_guests(user=Depends(get_current_user)):
    result = db_operations.show_guests()
    return JSONResponse(content=result)


@app.get("/search")
async def search_guest(request: Request, user=Depends(get_current_user)):
    data = await request.json()
    name = data.get("name")
    if not name:
        raise HTTPException(status_code=400, detail="Name is required")
    result = db_operations.search_name(name)
    return JSONResponse(content=result)


@app.get("/docs", include_in_schema=False)
async def get_documentation(request: Request):
    token = SessionManager.get_current_user(request)
    if token is None:
        return await auth_handler.login_redirect(request, "/docs")
    return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}
