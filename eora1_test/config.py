import os
from dotenv import load_dotenv

load_dotenv(override=True)

BOT_TOKEN = os.environ.get('BOT_TOKEN')

# webhook settings
WEBHOOK_HOST: str = "https://1987-176-59-174-229.eu.ngrok.io"
WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST: str = 'localhost'
WEBAPP_PORT: str = '5000'
