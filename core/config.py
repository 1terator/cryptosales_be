import os
from distutils.util import strtobool
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
load_dotenv()

# database
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "1234")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = int(os.environ.get("DB_PORT", 5432))
DB_NAME = os.environ.get("DB_NAME", "cryptosales")
# telegram
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
WEB_APPLICATION_URL = os.environ.get("WEB_APPLICATION_URL")
# webhook settings
USE_WEBHOOK = strtobool(os.environ.get("USE_WEBHOOK", False))
WEBHOOK_BASE_URL = os.environ.get("WEBHOOK_BASE_URL")
WEBHOOK_REQUESTS_PATH = os.environ.get("WEBHOOK_REQUESTS_PATH", "/webhook")
WEBHOOK_REQUESTS_HOST = os.environ.get("WEBHOOK_REQUESTS_HOST", "127.0.0.1")
WEBHOOK_REQUESTS_PORT = int(os.environ.get("WEBHOOK_REQUESTS_PORT", 8080))
WEBHOOK_SSL_FILE_PATH = os.environ.get("WEBHOOK_SSL_FILE_PATH")
# api settings
CRYPTOSALES_API_HOST = os.environ.get("CRYPTOSALES_API_HOST", "127.0.0.1")
CRYPTOSALES_API_PORT = int(os.environ.get("CRYPTOSALES_API_PORT", 80))
# localization
LOCALES_DIR = BASE_DIR / 'locales'
# jwt
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS256")
JWT_ACCESS_TOKEN_EXPIRES_MINUTES = int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES_MINUTES", 15))
