import os

from dotenv import load_dotenv
from redis.asyncio import Redis


# .env file se environment variables load karo
load_dotenv()


# Redis Cloud connection
redis_client = Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    username=os.getenv("REDIS_USERNAME"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)