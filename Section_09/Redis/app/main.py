from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends

from app.core.redis import redis_client

from app.middleware.rate_limiter import rate_limiter

from app.routes.products import router as product_router


# =========================================================
# STARTUP + SHUTDOWN
# =========================================================
#
# FastAPI application start hone par:
#     Redis connection check
#
# Application shutdown hone par:
#     Redis connection close
#
# =========================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    # =====================================================
    # STARTUP
    # =====================================================

    try:

        await redis_client.ping()

        print()
        print("======================================")
        print("✅ Redis connected successfully")
        print("======================================")
        print()

    except Exception as error:

        print()
        print("======================================")
        print("❌ Redis connection failed")
        print("======================================")
        print(error)
        print()

        raise error

    yield

    # =====================================================
    # SHUTDOWN
    # =====================================================

    await redis_client.aclose()

    print()
    print("======================================")
    print("Redis connection closed")
    print("======================================")
    print()


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="FastAPI + Redis",
    description="Redis caching and rate limiting example",
    version="1.0.0",
    lifespan=lifespan
)


# =========================================================
# HOME ROUTE
# =========================================================
#
# Maximum:
#     30 requests
#
# Time window:
#     5 minutes = 300 seconds
#
# =========================================================

@app.get(
    "/",
    dependencies=[
        Depends(
            rate_limiter(
                limit=30,
                timer=300,
                key="home"
            )
        )
    ]
)
async def home():

    return {
        "message": "FastAPI + Redis is working!"
    }


# =========================================================
# PRODUCT ROUTES
# =========================================================

app.include_router(
    product_router
)


# =========================================================
# REDIS TEST ROUTE
# =========================================================
#
# Ye simple endpoint Redis ke SET + GET ko test karta hai.
#
# =========================================================

@app.get("/redis-test")
async def redis_test():

    # Redis me value save karo
    await redis_client.set(
        "test_key",
        "Hello Redis"
    )

    # Redis se value read karo
    value = await redis_client.get(
        "test_key"
    )

    return {
        "redis": value
    }