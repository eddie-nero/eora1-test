from typing import Optional

import aioredis


class BaseRedis:
    def __init__(self, user: str, host: str, password: str = None, port: int = 6379, db: int = 0):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        if self.password:
            self.connection_uri = f"redis://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"
        else:
            self.connection_uri = f"redis://{self.host}:{self.port}/{self.db}"
        self._redis: Optional[aioredis.Redis] = None

    @property
    def closed(self):
        return not self._redis

    async def connect(self):
        if self.closed:
            self._redis = await aioredis.from_url(self.connection_uri)

    async def disconnect(self):
        if not self.closed:
            await self._redis.close()

    @property
    def redis(self) -> aioredis.Redis:
        if self.closed:
            raise RuntimeError("Redis connection is not opened")
        return self._redis
