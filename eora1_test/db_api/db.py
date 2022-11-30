import asyncpg
import asyncio

from eora1_test import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.POSTGRES_USER,
                password=config.POSTGRES_PASSWORD,
                host=config.POSTGRES_HOST,
                port=config.POSTGRES_PORT,
                database=config.POSTGRES_DB,
            )
        )

    async def save_message(self, telegram_id: int, msg: str):
        sql = "INSERT INTO messages (telegram_id, msg) VALUES ($1, $2)"
        await self.pool.execute(sql, telegram_id, msg)

    async def load_all_user_messages(self, telegram_id: int):
        sql = "SELECT msg FROM messages WHERE telegram_id={0}".format(telegram_id)
        result = await self.pool.fetch(sql)
        return [val.get('msg') for val in result]
    
    async def start_conversation(self, telegram_id):
        sql = "INSERT INTO conversations (telegram_id) VALUES ($1)"
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                try:
                    await connection.execute(sql, telegram_id)
                except Exception as e:
                    print(e)

    async def _create_table_messages(self):
        sql = """
        CREATE TABLE IF NOT EXISTS messages (
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER NOT NULL,
        msg TEXT NOT NULL,
        recieved_at TIMESTAMPTZ NOT NULL DEFAULT NOW())
        """
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(sql)

    async def _create_table_conversations(self):
        sql = """
        CREATE TABLE IF NOT EXISTS conversations (
        id SERIAL PRIMARY KEY,
        telegram_id INTEGER NOT NULL,
        is_shape_square BOOL,
        is_have_ears BOOL,
        started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        updated_at TIMESTAMPTZ)
        """
        async with self.pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(sql)

    async def create_tables(self):
        await self._create_table_messages()
        await self._create_table_conversations()
