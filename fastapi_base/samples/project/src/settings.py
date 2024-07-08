"""
App info, which includes in FastAPI object
e.g - app = FastAPI(title='my_app', version='0.1') e.t.c
"""

APP_VERSION = '0.1'
APP_TITLE = 'FastAPI app'
DESCRIPTION = 'Your desc'

# WARNING: change this to False on release
DEBUG = True

# url for openapi interactive docs
DOCS_URL = "/docs"
REDOC_URL = "/redoc"

# CORS settings
ALLOW_ORIGINS = ["*"]
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]
ALLOW_CREDENTIALS = True


# Database settings
DATABASE_URL ='sqlite+aiosqlite:///db.sqlite3'


