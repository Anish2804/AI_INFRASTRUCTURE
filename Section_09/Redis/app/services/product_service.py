import asyncio


# =========================================================
# GET ALL PRODUCTS
# =========================================================

async def get_products():
    """
    Ye function actual database/API ko represent karta hai.

    Abhi demonstration ke liye fake data return kar raha hai.

    2 seconds ka delay isliye hai taaki caching ka benefit
    clearly samajh aaye.
    """

    print("🐌 Fetching products from database/API...")

    # Slow database/API call simulate kar rahe hain.

    await asyncio.sleep(2)

    products = [
        {
            "id": 1,
            "name": "Laptop",
            "price": 50000
        },
        {
            "id": 2,
            "name": "Mobile",
            "price": 25000
        },
        {
            "id": 3,
            "name": "Keyboard",
            "price": 2000
        }
    ]

    return products


# =========================================================
# GET SINGLE PRODUCT
# =========================================================

async def get_product(product_id: int):
    """
    Ek single product ko database/API se fetch
    karne ka simulation.
    """

    print(
        f"🐌 Fetching product {product_id} "
        f"from database/API..."
    )

    await asyncio.sleep(2)

    return {
        "id": product_id,
        "name": f"Product {product_id}",
        "price": 1000
    }