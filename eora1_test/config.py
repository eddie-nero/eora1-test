import os
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# webhook settings
WEBHOOK_HOST: str = os.environ.get('WEBHOOK_HOST')
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST: str = '0.0.0.0'
WEBAPP_PORT: str = '5000'

# database settings
POSTGRES_USER: str = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', 'postgres')
POSTGRES_DB: str = os.environ.get('POSTGRES_DB', 'postgres')
POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT: int = int(os.environ.get('POSTGRES_PORT', 9999))

# redis settings
REDIS_USER: str = os.environ.get('REDIS_USER')
REDIS_PASSWORD: str = os.environ.get('REDIS_PASSWORD')
REDIS_HOST: str = os.environ.get("REDIS_HOST", default="localhost")
REDIS_PORT: int = int(os.environ.get("REDIS_PORT", default=6379))
REDIS_DB_FSM: int = int(os.environ.get("REDIS_DB_FSM", default=0))
