import asyncio

from cryptosales.api import start as api_start
from services.telegram.bot import start_polling


asyncio.run(start_polling())
