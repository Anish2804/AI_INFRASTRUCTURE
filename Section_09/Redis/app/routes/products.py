from fastapi import APIRouter, Depends

from app.middleware.rate_limiter import rate_limiter

from app.middleware.cache import (
    get_cached_data,
    set_cached_data
)

from app.services.product_service import (
    get_products,
    get_product
)


# =========================================================
# ROUTER
# =========================================================

router = APIRouter()


# =========================================================
# GET ALL PRODUCTS
# =========================================================

@router.get(
    "/products",

    # =====================================================
    # RATE LIMITER
    # =====================================================
    #
    # Maximum 5 requests
    # within 20 seconds.
    #
    # Node/Express middleware ka FastAPI equivalent:
    #
    # Depends(...)
    #
    # =====================================================

    dependencies=[
        Depends(
            rate_limiter(
                limit=5,
                timer=20,
                key="products"
            )
        )
    ]
)
async def products():

    # =====================================================
    # STEP 1: CHECK REDIS CACHE
    # =====================================================

    cached_products = await get_cached_data(
        "products"
    )

    # =====================================================
    # STEP 2: CACHE HIT
    # =====================================================

    if cached_products is not None:

        # Database/API ko call nahi karna.

        return {
            "source": "redis",
            "products": cached_products
        }

    # =====================================================
    # STEP 3: CACHE MISS
    # =====================================================

    # Redis me data nahi hai.
    #
    # Ab actual database/API ko call karenge.

    products_data = await get_products()

    # =====================================================
    # STEP 4: DATA KO REDIS ME CACHE KARO
    # =====================================================

    await set_cached_data(
        key="products",
        data=products_data,
        expiry=20
    )

    # =====================================================
    # STEP 5: RESPONSE
    # =====================================================

    return {
        "source": "database",
        "products": products_data
    }


# =========================================================
# GET SINGLE PRODUCT
# =========================================================

@router.get("/products/{product_id}")
async def product(product_id: int):

    # =====================================================
    # UNIQUE CACHE KEY
    # =====================================================
    #
    # /products/1
    #     ↓
    # product:1
    #
    # /products/2
    #     ↓
    # product:2
    #
    # =====================================================

    cache_key = f"product:{product_id}"

    # =====================================================
    # STEP 1: REDIS CACHE CHECK
    # =====================================================

    cached_product = await get_cached_data(
        cache_key
    )

    # =====================================================
    # STEP 2: CACHE HIT
    # =====================================================

    if cached_product is not None:

        return {
            "source": "redis",
            "product": cached_product
        }

    # =====================================================
    # STEP 3: CACHE MISS
    # =====================================================

    product_data = await get_product(
        product_id
    )

    # =====================================================
    # STEP 4: CACHE DATA
    # =====================================================

    await set_cached_data(
        key=cache_key,
        data=product_data,
        expiry=20
    )

    # =====================================================
    # STEP 5: RESPONSE
    # =====================================================

    return {
        "source": "database",
        "product": product_data
    }