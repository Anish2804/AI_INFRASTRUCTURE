import json

from app.core.redis import redis_client


# =========================================================
# GET DATA FROM CACHE
# =========================================================

async def get_cached_data(key: str):
    """
    Redis se data read karta hai.

    Agar data mil gaya:
        CACHE HIT

    Agar data nahi mila:
        CACHE MISS
    """

    # Redis GET command

    data = await redis_client.get(key)

    # =====================================================
    # CACHE MISS
    # =====================================================

    if data is None:

        print(f"❌ CACHE MISS: {key}")

        return None

    # =====================================================
    # CACHE HIT
    # =====================================================

    print(f"✅ CACHE HIT: {key}")

    # Redis me JSON string stored hai.
    #
    # JSON string → Python object

    return json.loads(data)


# =========================================================
# SAVE DATA TO CACHE
# =========================================================

async def set_cached_data(
    key: str,
    data,
    expiry: int
):
    """
    Data ko Redis me store karta hai.

    expiry:
        Kitne seconds baad cache automatically delete hoga.
    """

    # Python object → JSON string

    json_data = json.dumps(data)

    # =====================================================
    # SETEX
    # =====================================================
    #
    # SETEX ka matlab:
    #
    # SET + EXPIRY
    #
    # Example:
    #
    # products → JSON data → 20 seconds
    #
    # =====================================================

    await redis_client.setex(
        key,
        expiry,
        json_data
    )

    print(
        f"💾 CACHE SET: {key} "
        f"(expires in {expiry}s)"
    )