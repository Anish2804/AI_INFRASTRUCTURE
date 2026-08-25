from fastapi import Request, HTTPException

from app.core.redis import redis_client


def rate_limiter(
    limit: int,
    timer: int,
    key: str
):
    """
    Redis based rate limiter.

    limit:
        Kitni requests allow karni hain.

    timer:
        Kitne seconds ka time window hoga.

    key:
        Kis endpoint/application ke liye counter banana hai.
    """

    async def limiter(request: Request):

        # =================================================
        # STEP 1: CLIENT IP
        # =================================================
        #
        # Request kis client se aa rahi hai?
        #
        # Localhost par:
        #
        # 127.0.0.1
        #
        # =================================================

        client_ip = request.client.host

        # =================================================
        # STEP 2: UNIQUE REDIS KEY
        # =================================================
        #
        # Example:
        #
        # 127.0.0.1:products:request_count
        #
        # Har client ka alag counter rahega.
        #
        # =================================================

        redis_key = (
            f"{client_ip}:{key}:request_count"
        )

        # =================================================
        # STEP 3: INCREMENT REQUEST COUNT
        # =================================================
        #
        # Redis INCR:
        #
        # key nahi hai → 1
        # next request → 2
        # next request → 3
        #
        # =================================================

        request_count = await redis_client.incr(
            redis_key
        )

        # =================================================
        # STEP 4: FIRST REQUEST PAR EXPIRY SET
        # =================================================
        #
        # Sirf first request par timer set karenge.
        #
        # Agar timer = 20:
        #
        # 20 seconds ke baad counter automatically delete.
        #
        # =================================================

        if request_count == 1:

            await redis_client.expire(
                redis_key,
                timer
            )

        # =================================================
        # STEP 5: REMAINING TTL
        # =================================================

        time_remaining = await redis_client.ttl(
            redis_key
        )

        # =================================================
        # STEP 6: LIMIT CHECK
        # =================================================

        if request_count > limit:

            # HTTP 429 = Too Many Requests

            raise HTTPException(
                status_code=429,
                detail={
                    "message": "Too many requests",
                    "retry_after": time_remaining
                }
            )

    return limiter