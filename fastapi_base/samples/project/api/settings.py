APP_VERSION = '0.1'
APP_TITLE = 'FastAPI app'
DESCRIPTION = 'Your desc'

DEBUG = True

DOCS_URL = "/docs"
REDOC_URL = "/redoc"

# CORS settings
ALLOW_ORIGINS = ["*"]
ALLOW_METHODS = ["*"]
ALLOW_HEADERS = ["*"]
ALLOW_CREDENTIALS = True


# Database settings
ASYNC_DATABASE_URL ='sqlite+aiosqlite:///db.sqlite3'
SYNC_DATABASE_URL = 'sqlite:///db.sqlite3' 
