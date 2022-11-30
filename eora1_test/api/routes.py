from aiohttp import web

from eora1_test.api.handlers import welcome, start_bot


def setup_routes(app: web.Application):
    app.router.add_get('/', welcome)
    app.router.add_post('/start-bot/{user_id}', start_bot)
