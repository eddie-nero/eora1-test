from aiohttp import web


async def welcome(request):
    text = "Hello, user! Try /POST/{telegram_user_id} to /start-bot for start conversation"
    return web.Response(text=text)


async def start_bot(request):
    user = request.match_info.get('user_id')
    # msg = await request.text()
    return web.Response(text=f'Привет! Я помогу отличить кота от хлеба! Объект перед тобой квадратный?')
