# FastAPI + Redis

## Overview

This project demonstrates how Redis is integrated with FastAPI for two
common backend use cases:

1.  **Caching** -- store frequently requested product data in Redis so
    repeated requests are faster.
2.  **Rate limiting** -- count requests per client IP and reject
    requests that exceed a configured limit.

It also demonstrates Redis Cloud, async Redis operations,
TTL/expiration, Redis `SET`/`GET`, and testing through Swagger UI.

------------------------------------------------------------------------

## Project Structure

``` text
Redis/
├── .env
├── requirements.txt
├── .gitignore
└── app/
    ├── main.py
    ├── core/
    │   └── redis.py
    ├── middleware/
    │   ├── cache.py
    │   └── rate_limiter.py
    ├── routes/
    │   └── products.py
    └── services/
        └── product_service.py
```

### Responsibilities

-   `main.py` -- creates the FastAPI application, checks Redis on
    startup, closes Redis on shutdown, defines the home and Redis-test
    endpoints, and includes product routes.
-   `core/redis.py` -- creates the single async Redis client.
-   `middleware/cache.py` -- reads and writes JSON data to Redis with an
    expiry.
-   `middleware/rate_limiter.py` -- implements request counting and HTTP
    429 rate limiting.
-   `routes/products.py` -- contains product endpoints and combines
    caching with rate limiting.
-   `services/product_service.py` -- simulates a slow database/API.

------------------------------------------------------------------------

# Redis Connection

Redis Cloud credentials are stored in `.env`:

``` env
REDIS_HOST=your-redis-host
REDIS_PORT=19594
REDIS_USERNAME=default
REDIS_PASSWORD=your-redis-password
```

The `.env` file must not be committed to Git.

The application creates one shared async Redis client:

``` python
from redis.asyncio import Redis

redis_client = Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    username=os.getenv("REDIS_USERNAME"),
    password=os.getenv("REDIS_PASSWORD"),
    decode_responses=True,
)
```

`decode_responses=True` makes Redis return strings instead of bytes.

------------------------------------------------------------------------

# FastAPI Startup and Shutdown

FastAPI uses a lifespan function.

When the server starts:

``` python
await redis_client.ping()
```

checks whether Redis is reachable.

Successful startup prints:

``` text
Redis connected successfully
```

When FastAPI shuts down:

``` python
await redis_client.aclose()
```

closes the Redis client.

Flow:

``` text
FastAPI starts
      ↓
Redis PING
      ↓
Connection successful
      ↓
Application runs
      ↓
Application shuts down
      ↓
Redis connection closes
```

------------------------------------------------------------------------

# Endpoints

  Method   Endpoint                   Purpose
  -------- -------------------------- ------------------------------------------
  GET      `/`                        Home endpoint + rate limiting
  GET      `/redis-test`              Test Redis SET/GET
  GET      `/products`                Get all products + cache + rate limiting
  GET      `/products/{product_id}`   Get one product + cache

Swagger UI:

``` text
http://127.0.0.1:8000/docs
```

------------------------------------------------------------------------

# Redis Test

`GET /redis-test` verifies basic Redis communication.

The endpoint performs:

``` python
await redis_client.set("test_key", "Hello Redis")
value = await redis_client.get("test_key")
```

Expected response:

``` json
{
  "redis": "Hello Redis"
}
```

------------------------------------------------------------------------

# Product Caching

`GET /products` first checks Redis using the key:

``` text
products
```

## Cache MISS

If the key does not exist:

``` text
❌ CACHE MISS: products
      ↓
Slow database/API simulation
      ↓
Store result in Redis
      ↓
Return response
```

The simulated database/API waits for 2 seconds so the caching benefit is
easy to observe.

The response says:

``` json
{
  "source": "database"
}
```

## Cache HIT

If `products` already exists in Redis:

``` text
Redis
  ↓
CACHE HIT
  ↓
Return cached data
```

The database/API is not called.

The response says:

``` json
{
  "source": "redis"
}
```

------------------------------------------------------------------------

# Cache Expiration

Product data is cached for **20 seconds**.

The cache helper uses:

``` python
await redis_client.setex(
    key,
    expiry,
    json_data
)
```

`SETEX` stores the value and its expiration time together.

After 20 seconds, Redis automatically removes the key.

This gives:

``` text
Request 1
  ↓
CACHE MISS
  ↓
Database/API
  ↓
Redis cache (20 sec)
  ↓
Response

Request 2 within 20 sec
  ↓
CACHE HIT
  ↓
Redis
  ↓
Response

After 20 sec
  ↓
Cache expired
  ↓
Next request becomes CACHE MISS
```

------------------------------------------------------------------------

# Single Product Caching

`GET /products/{product_id}` creates a unique cache key.

Examples:

``` text
/products/1 → product:1
/products/2 → product:2
/products/3 → product:3
```

This keeps different products separate.

The first request for `/products/1` produces a cache miss; another
request within 20 seconds produces a cache hit.

------------------------------------------------------------------------

# Rate Limiting

The project uses Redis for request counting.

For `/products`:

``` text
5 requests / 20 seconds
```

For `/`:

``` text
30 requests / 5 minutes
```

The client IP is included in the Redis key.

For example:

``` text
127.0.0.1:products:request_count
```

Every request increments the counter:

``` text
Request 1 → 1
Request 2 → 2
Request 3 → 3
Request 4 → 4
Request 5 → 5
Request 6 → 6
```

The first request sets the expiration:

``` python
await redis_client.expire(redis_key, timer)
```

Once the counter exceeds the limit, FastAPI returns:

``` text
HTTP 429 Too Many Requests
```

Example:

``` json
{
  "detail": {
    "message": "Too many requests",
    "retry_after": 15
  }
}
```

------------------------------------------------------------------------

# Useful Redis CLI Commands

List all keys:

``` bash
KEYS *
```

Read a cached value:

``` bash
GET products
```

Read a single product:

``` bash
GET product:1
```

Read the rate-limit counter:

``` bash
GET 127.0.0.1:products:request_count
```

Check remaining cache TTL:

``` bash
TTL products
```

Check rate-limit TTL:

``` bash
TTL 127.0.0.1:products:request_count
```

`TTL` returns the remaining lifetime in seconds.

------------------------------------------------------------------------

# How to Run

Activate the virtual environment:

``` bash
source .venv/bin/activate
```

Start FastAPI:

``` bash
uvicorn app.main:app --reload
```

Open:

``` text
http://127.0.0.1:8000/docs
```

Then test the endpoints from Swagger UI.

------------------------------------------------------------------------

# Testing Checklist

### 1. FastAPI

Call:

``` text
GET /
```

Expected:

``` json
{
  "message": "FastAPI + Redis is working!"
}
```

### 2. Redis Connection

Call:

``` text
GET /redis-test
```

Expected:

``` json
{
  "redis": "Hello Redis"
}
```

### 3. Products Cache MISS

First call:

``` text
GET /products
```

Expected terminal:

``` text
CACHE MISS: products
Fetching products from database/API...
CACHE SET: products (expires in 20s)
```

### 4. Products Cache HIT

Call `/products` again within 20 seconds.

Expected:

``` text
CACHE HIT: products
```

### 5. Cache Expiry

Wait 20 seconds and call `/products` again.

Expected:

``` text
CACHE MISS: products
```

### 6. Single Product

Call:

``` text
GET /products/1
```

Then call it again within 20 seconds.

Expected:

``` text
CACHE MISS: product:1
```

followed by:

``` text
CACHE HIT: product:1
```

### 7. Rate Limiting

Call `/products` more than 5 times within 20 seconds.

The request that exceeds the limit should return:

``` text
429 Too Many Requests
```

------------------------------------------------------------------------

# Important Cleanup

The final project uses **one Redis client**:

``` python
from app.core.redis import redis_client
```

Do not create a second Redis client in `main.py`.

Also, the `/` route must be defined only once. The earlier duplicate
route caused:

``` text
Duplicate Operation ID home_get
```

The Redis test endpoint should use the same async client:

``` python
await redis_client.set(...)
await redis_client.get(...)
```

rather than a separate synchronous client.

------------------------------------------------------------------------

# Complete Request Flow

For `/products` on a first request:

``` text
Client
  ↓
FastAPI
  ↓
Rate Limiter
  ↓
Redis request counter
  ↓
Cache Check
  ↓
CACHE MISS
  ↓
Product Service
  ↓
Slow database/API simulation
  ↓
Redis SETEX (20 seconds)
  ↓
Response
```

For a repeated request within 20 seconds:

``` text
Client
  ↓
FastAPI
  ↓
Rate Limiter
  ↓
Redis Cache
  ↓
CACHE HIT
  ↓
Response
```

The slow database/API is skipped.

------------------------------------------------------------------------

# Node.js Concept vs FastAPI Concept

The backend concept implemented by the original Node.js version is
reproduced here using FastAPI.

Conceptually:

``` text
Node.js / Express
        ↓
Middleware
        ↓
Redis
```

becomes:

``` text
FastAPI
        ↓
Depends / application logic
        ↓
Redis
```

The framework syntax changes, but the backend concepts remain the same:

-   Redis connection
-   Caching
-   Cache HIT / MISS
-   TTL
-   Rate limiting
-   Request counters
-   HTTP 429
-   API responses

------------------------------------------------------------------------

# Security

Never commit Redis credentials.

`.gitignore` should contain at least:

``` gitignore
.env
.venv/
__pycache__/
*.pyc
```

If a Redis password is exposed publicly, rotate it immediately.

------------------------------------------------------------------------

# Final Summary

This project is a working FastAPI + Redis backend demonstrating:

-   Redis Cloud connection
-   Async Redis client
-   Startup/shutdown connection management
-   Redis `SET` and `GET`
-   Product caching
-   Cache HIT and MISS
-   20-second cache expiration
-   Dynamic product cache keys
-   Redis-based rate limiting
-   Request counters using `INCR`
-   Expiration using `EXPIRE`
-   TTL inspection
-   HTTP 429 handling
-   Swagger-based API testing

The core idea is simple:

``` text
FastAPI
   │
   ├── Rate Limiting ──→ Redis
   │
   ├── Cache ──────────→ Redis
   │
   └── Cache MISS ────→ Database/API
```

Redis therefore acts as both the **fast cache layer** and the
**request-counter/rate-limiting layer**.
