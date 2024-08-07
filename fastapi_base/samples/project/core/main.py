# delete any if you don't need it
from contextlib import asynccontextmanager # delete if you using alembic
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

# import from your apps routers
# e.g. - from core.your_app.views import my_router

# import base settings
from core.settings import (
    APP_VERSION,
    APP_TITLE,
    DEBUG,
    DESCRIPTION,
    DOCS_URL,
    REDOC_URL,
    ALLOW_METHODS,
    ALLOW_HEADERS,
    ALLOW_CREDENTIALS,
    ALLOW_ORIGINS,
)

# WARNING: delete it if you using alembic
import core.models_imports # noqa
from core.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield


# creating app with base settings
app = FastAPI(
    title=APP_TITLE,
    version=APP_VERSION,
    debug=DEBUG,
    description=DESCRIPTION,
    docs_url=DOCS_URL,
    redoc_url=REDOC_URL,
    lifespan=lifespan # WARNING: delete if you using alembic
)

# add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=ALLOW_CREDENTIALS,
    allow_methods=ALLOW_METHODS,
    allow_headers=ALLOW_HEADERS,
)

# add routers to app
# list of routers to include in app
# e.g. routers = [my_app_router, users_router, auth_router]
routers = []
for router in routers:
    app.include_router(router)
