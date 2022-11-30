from aiohttp import web
from eora1_test.loader import db


async def welcome(request):
    text = "Hello, user! Try /POST/{telegram_user_id} to /start-bot for start conversation"
    return web.Response(text=text)


async def start_bot(request):
    user = request.match_info.get('user_id')
    # msg = await request.text()
    await db.start_conversation(user)
    return web.Response(text=f'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
