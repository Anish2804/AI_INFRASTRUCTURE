FastAPI Mastery — Complete Course & Revision Notes

A complete revision-first README covering the full 31-topic FastAPI
course, from APIs and routing to PostgreSQL, authentication, testing,
caching, rate limiting, deployment, and the final Blog API.

📚 Course Roadmap

Introduction to APIs & Backend Development

Introduction to FastAPI & Performance Comparisons

Prerequisites, Setup & Environment

Basic Routing & GET Requests

Dynamic Routing & Path Parameters

Query Parameters

Request Body & POST Requests

Advanced Pydantic: Nested Models

CRUD --- In-Memory Todo App

Combining Path, Query & Body Parameters

Response Models

Status Codes & HTTPException

Advanced Exception Handling

Dependency Injection

Middleware

SQLite, ORM & SQLAlchemy

SQLAlchemy CRUD

Async Programming

Authentication & JWT

OAuth2 & Password Hashing

File Uploads & Static Assets

CORS

Environment Variables & Configuration

Testing with PyTest

Third-Party API Integration

Web Crawling & Scraping

Pagination

Caching

Rate Limiting

Deployment on Render

Capstone --- PostgreSQL Blog API

Topics

1. Introduction to APIs & Backend Development

Concepts Covered

What is Backend?

What is an API?

Why use an API?

JSON

HTTP Methods

What is Backend?

Backend is the server-side part of an application. It receives requests
from clients, executes business logic, communicates with databases or
external services, and sends responses back.

Frontend / Client
       ↓
     HTTP
       ↓
    Backend
       ↓
 Business Logic
       ↓
   Database
       ↓
    Backend
       ↓
 JSON Response
       ↓
Frontend / Client

What is an API?

API = Application Programming Interface

An API is a defined interface through which one software component
communicates with another.

In a typical web application:

React / Mobile App
        ↓
       API
        ↓
     FastAPI
        ↓
    PostgreSQL

The API acts as the communication layer between the client and backend
services.

Why use an API?

Separate frontend and backend

Allow multiple clients to use the same backend

Standardize communication

Expose data and business operations

Integrate external services

JSON

JSON is a common data format for APIs.

{
  "id": 1,
  "name": "Anish",
  "email": "anish@example.com"
}

HTTP Methods

Method   Main Purpose

GET      Read/fetch data
POST     Create/submit data
PUT      Replace/update a resource
PATCH    Partially update a resource
DELETE   Delete a resource

Easy Memory

POST   → Create
GET    → Read
PUT    → Replace
PATCH  → Partial Update
DELETE → Delete

2. Introduction to FastAPI

Concepts Covered

What is FastAPI?

Why FastAPI?

FastAPI vs Flask vs Django

FastAPI Core Idea

What is FastAPI?

FastAPI is a modern Python web framework designed for building APIs and
backend applications.

Its important characteristics include:

High performance

Type-hint based development

Automatic validation through Pydantic

Automatic API documentation

Async/await support

Dependency Injection

OpenAPI support

Why FastAPI?

FastAPI is particularly useful when building:

REST APIs

Microservices

Backend services

Authentication systems

Database-backed applications

AI/ML APIs

High-concurrency I/O applications

FastAPI vs Flask vs Django

Feature           FastAPI           Flask               Django

Style             API-focused       Micro-framework     Full-stack framework

Async support     Strong            Available           Available

Validation        Pydantic          Mostly              Django ecosystem
manual/extensions

Automatic API     Yes               Not by default      Not by default
docs

Performance focus High              Lightweight         More
batteries-included

FastAPI Core Idea

Python Type Hints
       ↓
FastAPI
       ↓
Pydantic Validation
       ↓
OpenAPI Schema
       ↓
Swagger / ReDoc

3. Prerequisites, Setup & Environment

Concepts Covered

Prerequisites

Virtual Environment

Create VENV

Install FastAPI + Uvicorn

First FastAPI Application

Run Server

Swagger UI

ReDoc

Professional Structure

Prerequisites

The course assumes basic Python knowledge.

You should be comfortable with:

Variables

Functions

Lists/dictionaries

Classes

Exceptions

Imports

Basic type hints

Virtual Environment

A virtual environment isolates project dependencies.

Without isolation:

Project A → Package Version X
Project B → Package Version Y
        ↓
Potential conflicts

With virtual environments:

Project A → Own Environment
Project B → Own Environment

Create VENV

python -m venv venv

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

Install FastAPI + Uvicorn

pip install fastapi uvicorn

First FastAPI Application

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

Run Server

uvicorn main:app --reload

Meaning:

main → main.py
app  → FastAPI object
--reload → development auto-reload

Swagger UI

FastAPI automatically provides interactive documentation:

/docs

Example:

http://127.0.0.1:8000/docs

ReDoc

/redoc

Professional Structure

A growing project should separate concerns:

project/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── routers/
│   └── services/
├── tests/
├── static/
├── .env
├── .gitignore
├── requirements.txt
└── README.md

4. Basic Routing & GET Requests

Concepts Covered

What is a Route?

Multiple Routes

Endpoint

Swagger Testing

What is a Route?

A route connects an HTTP method + URL path to a Python function.

@app.get("/")
def home():
    return {"message": "Home"}

Here:

GET + /
   ↓
home()

Multiple Routes

@app.get("/")
def home():
    return {"message": "Home"}

@app.get("/about")
def about():
    return {"message": "About"}

@app.get("/users")
def users():
    return {"users": []}

Endpoint

An endpoint is a callable API operation exposed at a particular route.

Example:

GET /users

Swagger Testing

Swagger allows you to:

Open /docs

Select an endpoint

Click Try it out

Enter parameters

Execute

Inspect response/status code

5. Dynamic Routing & Path Parameters

Concepts Covered

What is a Path Parameter?

Why Path Parameters?

Type Validation

Path vs Query

What is a Path Parameter?

A path parameter is a dynamic value embedded inside the URL path.

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

Request:

GET /users/10

Response:

{
  "user_id": 10
}

Why Path Parameters?

Use them when identifying a specific resource.

Examples:

/users/10
/products/25
/orders/500
/blogs/7

Type Validation

user_id: int

FastAPI uses the type information to validate the input.

/users/10   → valid
/users/abc  → validation error

Path vs Query

/users/10

10 identifies a specific resource.

/users?age=20

age=20 filters/customizes a collection.

6. Query Parameters

Concepts Covered

What is a Query Parameter?

Multiple Query Parameters

Optional Query Parameter

Default Values

Common Uses

What is a Query Parameter?

Query parameters are key-value pairs after ?.

/products?price=1000

Example:

@app.get("/products")
def products(price: int):
    return {"price": price}

Multiple Query Parameters

/products?name=laptop&price=50000

@app.get("/products")
def products(name: str, price: int):
    return {
        "name": name,
        "price": price
    }

Optional Query Parameter

@app.get("/products")
def products(name: str | None = None):
    return {"name": name}

Now:

/products

is valid.

Default Values

@app.get("/products")
def products(limit: int = 10):
    return {"limit": limit}

If the client does not send limit, the value is 10.

Common Uses

Search

Filtering

Sorting

Pagination

Optional behavior

Limits/offsets

Memory Trick

Path parameter
→ Which resource?

Query parameter
→ How should I filter/customize the resource?

7. Request Body & POST Requests

Concepts Covered

What is a Request Body?

Pydantic BaseModel

Pydantic vs Dict

Why Request Schemas?

What is a Request Body?

Request body is data sent by the client inside an HTTP request.

Commonly used with:

POST

PUT

PATCH

Example:

{
  "name": "Anish",
  "email": "anish@gmail.com",
  "age": 23
}

Pydantic BaseModel

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int

Use it in a route:

@app.post("/users")
def create_user(user: User):
    return user

Pydantic vs Dict

Dict

data = {
    "name": "Anish",
    "age": "wrong"
}

You must validate manually.

Pydantic

class User(BaseModel):
    name: str
    age: int

FastAPI validates the request against the schema.

Why Request Schemas?

Validate input

Define expected structure

Improve API documentation

Reduce manual validation

Make code predictable

8. Advanced Pydantic --- Nested Models

Concepts Covered

Nested Model

Why Nested Models?

Core Pydantic Concept

Nested Model

A Pydantic model can contain another Pydantic model.

from pydantic import BaseModel

class Address(BaseModel):
    city: str
    pin: int

class User(BaseModel):
    name: str
    address: Address

JSON:

{
  "name": "Anish",
  "address": {
    "city": "Bhagalpur",
    "pin": 812001
  }
}

Why Nested Models?

Real applications contain hierarchical data.

Examples:

User
 ├── name
 ├── email
 └── address
      ├── city
      └── pin

Other examples:

Order
 ├── customer
 ├── items[]
 └── shipping_address

Core Pydantic Concept

Raw JSON
   ↓
Pydantic Schema
   ↓
Validation + Parsing
   ↓
Python Object

9. CRUD --- In-Memory Todo App

Concepts Covered

CRUD

In-Memory Storage

Create

Read All

Read One

Update

Delete

PUT vs PATCH

Testing Tools

CRUD

CRUD means:

C → Create
R → Read
U → Update
D → Delete

Mapping:

CREATE → POST
READ   → GET
UPDATE → PUT/PATCH
DELETE → DELETE

In-Memory Storage

For learning, a Python list can behave like a temporary database:

todos = []

Important:

In-memory data is temporary and normally disappears when the process
restarts.

Create

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

Read All

@app.get("/todos")
def get_todos():
    return todos

Read One

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )

Update

Concept:

Find item
   ↓
Modify/replace fields
   ↓
Return updated item

Delete

For a Python list:

todos.pop(index)

PUT vs PATCH

PUT

Generally represents complete replacement of a resource.

PUT /users/10

PATCH

Generally represents partial modification.

PATCH /users/10

Example:

{
  "email": "new@example.com"
}

Only the email may be changed.

Testing Tools

The course uses client tools such as:

Swagger UI

Postman

Thunder Client

10. Combining Path, Query & Body Parameters

One endpoint can receive different kinds of input.

Example:

@app.put("/users/{user_id}")
def update_user(
    user_id: int,
    notify: bool = False,
    user: User = ...
):
    ...

Conceptually:

/users/10?notify=true
       ↑         ↑
       │         Query
       │
       Path

Body:
{
  "name": "Anish"
}

Concepts Covered

Remember

Remember

Path
→ resource identity

Query
→ optional/filter/control information

Body
→ structured resource data

11. Response Models

Concepts Covered

What is a Response Model?

Why Separate Request and Response Models?

Benefits

What is a Response Model?

A response model defines the shape of data returned to the client.

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

Route:

@app.post(
    "/users",
    response_model=UserResponse
)
def create_user(user: UserCreate):
    ...

Why Separate Request and Response Models?

Suppose database data contains:

{
  "id": 1,
  "name": "Anish",
  "email": "anish@gmail.com",
  "password": "hashed-password"
}

The API should not expose password data unnecessarily.

UserCreate
→ What client is allowed to send

UserResponse
→ What client is allowed to receive

Benefits

Output validation

Data filtering

Sensitive field protection

Consistent API responses

Better documentation

12. HTTP Status Codes & HTTPException

Concepts Covered

Status Code Categories

Important Codes

HTTPException

Why HTTPException?

Status Code Categories

1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error

Important Codes

Code   Meaning                 Common Use

200    OK                      Successful request
201    Created                 Resource created
204    No Content              Successful request without body
400    Bad Request             Invalid request
401    Unauthorized            Authentication required/invalid
403    Forbidden               Authenticated but not allowed
404    Not Found               Resource doesn't exist
409    Conflict                Resource/state conflict
422    Validation Error        Request validation failed
429    Too Many Requests       Rate limit exceeded
500    Internal Server Error   Server-side failure

HTTPException

from fastapi import HTTPException

raise HTTPException(
    status_code=404,
    detail="User not found"
)

Why HTTPException?

It allows the API to stop normal processing and return a proper HTTP
error response.

13. Advanced Exception Handling

Concepts Covered

Custom Exception

Global Handler

Why Global Handlers?

Custom Exception

Create domain-specific errors:

class UserNotFoundException(Exception):
    pass

Global Handler

@app.exception_handler(UserNotFoundException)
async def user_not_found_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"detail": "User not found"}
    )

Why Global Handlers?

Without global handling:

Route A → error handling
Route B → same error handling
Route C → same error handling

With centralized handling:

Any route
   ↓
Raises Custom Exception
   ↓
Global Handler
   ↓
Standard Response

Benefits:

Less duplicate code

Consistent errors

Easier maintenance

Better scalability

14. Dependency Injection

Concepts Covered

What is Dependency Injection?

Basic Example

Why DI?

DB Example

Key Idea

What is Dependency Injection?

Dependency Injection means a function receives the
functionality/resources it needs from an external dependency provider
instead of creating everything itself.

FastAPI provides:

Depends

Basic Example

from fastapi import Depends

def get_current_user():
    return {"name": "Anish"}

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user

Flow:

Request
   ↓
Depends(get_current_user)
   ↓
get_current_user()
   ↓
profile(user)

Why DI?

Common reusable dependencies:

Current user

Database session

Authentication

Authorization

Common headers

Shared validation

Pagination logic

DB Example

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Then:

@app.get("/users")
def users(db: Session = Depends(get_db)):
    ...

Key Idea

Dependency
→ reusable logic/resource

Depends()
→ asks FastAPI to provide it

15. Middleware

Concepts Covered

What is Middleware?

call_next

Timing Middleware

Middleware vs Dependency

What is Middleware?

Middleware is a layer that runs around the request/response lifecycle.

Client
  ↓
Middleware
  ↓
Route
  ↓
Middleware
  ↓
Client

call_next

Typical middleware:

@app.middleware("http")
async def middleware(request, call_next):
    response = await call_next(request)
    return response

call_next(request) passes the request to the next layer/route and
returns its response.

Timing Middleware

import time

@app.middleware("http")
async def timing_middleware(request, call_next):
    start = time.time()

    response = await call_next(request)

    duration = time.time() - start
    print(request.url.path, duration)

    return response

Useful for:

Logging

Latency measurement

Monitoring

Global headers

Request/response processing

Middleware vs Dependency

Middleware                     Dependency

Global/request lifecycle       Selected routes
Runs around request/response   Injects reusable logic
Logging                        Authentication
Timing                         DB session
Global processing              Current user

Memory Trick

Global concern → Middleware
Reusable route dependency → Depends

16. SQLite, ORM & SQLAlchemy

Concepts Covered

SQLite

Raw SQLite

ORM

Raw SQL vs ORM

SQLAlchemy

Engine

Session

Base Model

Safe DB Dependency

SQLite

SQLite is a lightweight, file-based relational database.

Characteristics:

No separate database server required

Easy local setup

Useful for learning/prototypes

Built into Python through sqlite3

Raw SQLite

import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()

Raw SQL can then be executed.

Example:

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT
);

ORM

ORM = Object Relational Mapping.

It maps programming-language objects/classes to relational database
structures.

Python Class  ↔ Database Table
Object        ↔ Row
Attribute     ↔ Column

Raw SQL vs ORM

Raw SQL

SELECT * FROM users WHERE id = 1;

ORM-style idea

db.query(User).filter(User.id == 1).first()

ORM benefits:

Object-oriented interface

Reusable models

Less repetitive SQL

Easier integration with application code

SQLAlchemy

SQLAlchemy is a Python SQL toolkit and ORM.

Typical architecture:

FastAPI
   ↓
SQLAlchemy
   ↓
PostgreSQL / SQLite

Engine

The SQLAlchemy engine manages the database connectivity infrastructure.

engine = create_engine(DATABASE_URL)

Session

A session is used to interact with the database during application
operations.

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base Model

SQLAlchemy models are normally derived from a declarative base.

Base = declarative_base()

Safe DB Dependency

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

Why yield?

It lets FastAPI provide the resource to the route and then continue
cleanup after the route finishes.

Why finally?

The database session should be closed even when an error occurs.

17. SQLAlchemy CRUD

Concepts Covered

Database Model

CREATE

READ ALL

READ BY ID

UPDATE

DELETE

CRUD Lifecycle

Database Model

Example:

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

CREATE

user = User(
    name="Anish",
    email="anish@gmail.com"
)

db.add(user)
db.commit()
db.refresh(user)

db.add()

Adds the object to the current session.

db.commit()

Commits the transaction.

db.refresh()

Refreshes the object using current database state.

READ ALL

users = db.query(User).all()

READ BY ID

user = (
    db.query(User)
    .filter(User.id == user_id)
    .first()
)

If not found:

raise HTTPException(
    status_code=404,
    detail="User not found"
)

UPDATE

user.name = "New Name"

db.commit()
db.refresh(user)

DELETE

db.delete(user)
db.commit()

CRUD Lifecycle

Request
  ↓
Pydantic validation
  ↓
SQLAlchemy model/query
  ↓
Session
  ↓
Database
  ↓
Commit/refresh
  ↓
Response

18. Asynchronous Programming

Concepts Covered

Synchronous

Asynchronous

async def

await

asyncio

Important Concept

Synchronous

Synchronous execution generally waits for an operation before moving on.

Task A
 ↓
Wait
 ↓
Task B
 ↓
Wait
 ↓
Task C

Asynchronous

Async programs can switch to other work while waiting for asynchronous
I/O.

Task A starts
 ↓
A waits for I/O
 ↓
Task B runs
 ↓
B waits
 ↓
Task C runs

async def

Defines a coroutine function.

async def get_data():
    ...

await

Suspends the current coroutine until an awaited async operation
completes.

result = await some_async_operation()

asyncio

Python's built-in asyncio module provides infrastructure for
asynchronous programming.

import asyncio

async def main():
    await asyncio.sleep(1)

Important Concept

Async is especially useful for I/O-bound workloads such as:

Network requests

Async database operations

File/network I/O

Waiting for external services

Async does not automatically make CPU-heavy work faster.

19. Authentication & JWT

Concepts Covered

Authentication

Authorization

JWT

JWT Structure

Important

python-jose

JWT Authentication Flow

Expiration

Authentication

Authentication answers:

Who are you?

Example:

Email + Password
      ↓
Verify
      ↓
Authenticated User

Authorization

Authorization answers:

What are you allowed to do?

Example:

Normal User → Read own profile
Admin       → Manage users

JWT

JWT = JSON Web Token.

JWT is commonly used to represent signed authentication information
between client and server.

JWT Structure

Header.Payload.Signature

Header

Contains metadata such as algorithm/type.

{
  "alg": "HS256",
  "typ": "JWT"
}

Payload

Contains claims.

{
  "sub": "123",
  "exp": 1234567890
}

Signature

Used to verify token integrity/authenticity.

Important

JWT payload is encoded, not automatically encrypted.

Do not place secrets/passwords inside a JWT payload.

python-jose

The course uses python-jose for JWT encoding/decoding.

Concept:

token = jwt.encode(
    payload,
    SECRET_KEY,
    algorithm="HS256"
)

Decode:

payload = jwt.decode(
    token,
    SECRET_KEY,
    algorithms=["HS256"]
)

JWT Authentication Flow

LOGIN
  ↓
Verify Credentials
  ↓
Generate JWT
  ↓
Return Access Token
  ↓
Client Stores Token
  ↓
Client Sends Bearer Token
  ↓
Backend Verifies Token
  ↓
Identify User
  ↓
Protected Route

Typical header:

Authorization: Bearer <token>

Expiration

Tokens can contain an expiration claim.

Expired tokens should be rejected.

20. OAuth2 & Password Hashing

Concepts Covered

Why Plain Text Passwords Are Dangerous

Password Hashing

Bcrypt

Authentication vs Encryption

OAuth2 Password Bearer Flow

Bearer Token

Swagger Authorization

Protected Route

Why Plain Text Passwords Are Dangerous

Never store:

password123

directly in the database.

If the database leaks, plain-text passwords are immediately exposed.

Password Hashing

Concept:

Plain Password
      ↓
Hash Function
      ↓
Password Hash
      ↓
Database

During login:

Entered Password
      ↓
Verify against stored hash
      ↓
Match / Reject

Bcrypt

The course uses:

passlib[bcrypt]

for password hashing/verification.

Authentication vs Encryption

Hashing

One-way transformation

Encryption

Data can be decrypted with the appropriate key

Passwords should normally be stored using password hashing, not
reversible encryption.

OAuth2 Password Bearer Flow

FastAPI provides security utilities such as:

OAuth2PasswordRequestForm

Typical token response:

{
  "access_token": "....",
  "token_type": "bearer"
}

Bearer Token

Client sends:

Authorization: Bearer <access_token>

Swagger Authorization

FastAPI's Swagger UI can expose an authorization interface so you can
enter a token and test protected endpoints.

Protected Route

@app.get("/profile")
def profile(
    current_user = Depends(get_current_user)
):
    return current_user

Flow:

Request
 ↓
Bearer Token
 ↓
Dependency
 ↓
JWT Verification
 ↓
Current User
 ↓
Protected Endpoint

21. File Uploads & Static Assets

Concepts Covered

UploadFile

Why UploadFile?

Multipart Form

Saving Files

Directory Creation

Static Files

File Not Found

UploadFile

FastAPI provides:

from fastapi import UploadFile, File

Example:

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    return {"filename": file.filename}

Why UploadFile?

Useful for:

Images

PDFs

Documents

User uploads

Multipart Form

File uploads commonly use multipart/form-data.

Saving Files

Concept:

with open(path, "wb") as buffer:
    buffer.write(await file.read())

wb means binary write mode.

Directory Creation

You can create an upload directory if it doesn't exist.

from pathlib import Path

Path("media").mkdir(
    parents=True,
    exist_ok=True
)

Static Files

FastAPI can mount a directory:

from fastapi.staticfiles import StaticFiles

app.mount(
    "/media",
    StaticFiles(directory="media"),
    name="media"
)

Now files can be exposed under /media/....

File Not Found

If an application provides a custom file-serving endpoint, it should
check whether the requested file exists and return an appropriate error
if it does not.

22. CORS

Concepts Covered

What is CORS?

CORSMiddleware

Important CORS Concepts

React + FastAPI

What is CORS?

CORS = Cross-Origin Resource Sharing.

It is a browser security mechanism that controls requests made from one
origin to another origin.

Example:

Frontend:
http://localhost:5173

Backend:
http://localhost:8000

Different origins can trigger CORS restrictions in browsers.

CORSMiddleware

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

Important CORS Concepts

Origin

An origin is determined by:

scheme + host + port

Example:

http://localhost:5173

Common Configuration

allow_origins

allow_methods

allow_headers

credentials configuration when needed

React + FastAPI

Typical development architecture:

React / Vite
localhost:5173
      ↓
HTTP Request
      ↓
FastAPI
localhost:8000
      ↓
JSON Response
      ↓
React

23. Environment Variables & Configuration

Concepts Covered

Why Environment Variables?

python-dotenv

Centralized Configuration

.gitignore

Golden Rule

Why Environment Variables?

Never hardcode sensitive or environment-specific values such as:

Database URL

Database password

JWT secret

API keys

Deployment-specific configuration

Bad:

SECRET_KEY = "my-secret"

Better:

.env

Example:

DATABASE_URL=...
SECRET_KEY=...

python-dotenv

The course uses:

python-dotenv

to load environment variables.

Concept:

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

Centralized Configuration

A project can keep configuration in a dedicated file such as:

config.py

Example idea:

class Settings:
    DATABASE_URL = ...
    SECRET_KEY = ...

.gitignore

Important entries:

.env
venv/
__pycache__/
*.pyc

Golden Rule

Secrets
  ↓
Environment Variables
  ↓
Application

Not:

Secrets
  ↓
GitHub source code

24. API Testing with PyTest

Concepts Covered

Why Testing?

PyTest

FastAPI TestClient

Test Endpoint

Test JSON

What to Test?

Why Testing?

Testing verifies that code behaves as expected.

Without tests:

Change Code
 ↓
Hope Nothing Broke

With tests:

Change Code
 ↓
Run Tests
 ↓
Detect Regression

PyTest

Install:

pip install pytest

Basic test:

def test_addition():
    assert 1 + 1 == 2

FastAPI TestClient

FastAPI provides a test client for making test requests against the
application.

Concept:

from fastapi.testclient import TestClient

client = TestClient(app)

Test Endpoint

def test_home():
    response = client.get("/")

    assert response.status_code == 200

Test JSON

def test_home():
    response = client.get("/")

    assert response.json() == {
        "message": "Hello World"
    }

What to Test?

Status codes

Response JSON

Validation errors

Authentication

CRUD behavior

Edge cases

Not-found cases

Permission behavior

25. Third-Party API Integration

Concepts Covered

What is a Third-Party API?

requests

Example Flow

Things to Handle

What is a Third-Party API?

An external API owned/provided by another service.

Architecture:

Client
  ↓
Your FastAPI
  ↓
Third-Party API
  ↓
External Response
  ↓
Your FastAPI
  ↓
Client

requests

The course uses Python's requests package for external HTTP requests.

import requests

response = requests.get(
    "https://example.com/api"
)

data = response.json()

Example Flow

GET /external-data
       ↓
FastAPI
       ↓
requests.get(...)
       ↓
External API
       ↓
JSON
       ↓
FastAPI
       ↓
Client

Things to Handle

Production integrations should consider:

Timeout

Connection errors

Non-2xx responses

Rate limits

Invalid JSON

Authentication

Retries where appropriate

26. Web Crawling & Scraping

Concepts Covered

What is Web Scraping?

Flow

Example

find_all()

CSS Classes / Tags

Important Legal/Technical Considerations

What is Web Scraping?

Web scraping means extracting information from web pages
programmatically.

Typical stack:

requests
+
BeautifulSoup4

Flow

Website
  ↓
requests.get()
  ↓
HTML
  ↓
BeautifulSoup
  ↓
Parse HTML
  ↓
Extract Elements

Example

import requests
from bs4 import BeautifulSoup

response = requests.get(url)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

headlines = soup.find_all("h2")

find_all()

Used to locate multiple matching HTML elements.

Examples:

soup.find_all("h2")
soup.find_all("a")
soup.find_all(class_="headline")

CSS Classes / Tags

Scraping often relies on:

HTML tags

CSS classes

IDs

Attributes

Important Legal/Technical Considerations

Before scraping:

Check the site's terms

Respect applicable robots rules

Respect rate limits

Avoid excessive traffic

Check whether permission is required

Follow applicable laws

27. Pagination

Concepts Covered

Why Pagination?

Query Parameters

Offset Formula

Typical Database Query

Pagination Response

Important Metadata

Pagination + Search

Why Pagination?

Suppose a database has:

1,000,000 records

Returning all of them in one response is inefficient.

Instead:

Page 1 → 20 records
Page 2 → 20 records
Page 3 → 20 records
...

Query Parameters

Example:

GET /users?page=2&limit=20

Offset Formula

The standard offset formula is:

offset = (page - 1) * limit

Example:

page = 3
limit = 20

offset = (3 - 1) * 20
       = 40

Typical Database Query

Conceptually:

offset = (page - 1) * limit

items = (
    db.query(User)
    .offset(offset)
    .limit(limit)
    .all()
)

Pagination Response

{
  "page": 2,
  "limit": 20,
  "total": 100,
  "data": []
}

Important Metadata

Useful pagination responses can include:

Current page

Page size/limit

Total records

Current data

Pagination + Search

Example:

/blogs?search=fastapi&page=2&limit=10

Meaning:

search → filter
page   → page number
limit  → page size

28. Caching

Concepts Covered

What is Caching?

Common Use Cases

TTL

Basic Cache Concept

Cache Hit vs Cache Miss

Why Cache?

What is Caching?

Caching stores previously computed/fetched data temporarily so future
requests can be served faster.

Without cache:

Request
 ↓
Expensive Operation
 ↓
External API / Scraping / DB
 ↓
Slow Response

With cache:

Request
 ↓
Cache Hit
 ↓
Fast Response

Common Use Cases

Expensive database queries

External API responses

Scraped data

Computed results

Frequently requested resources

TTL

TTL = Time To Live

It defines how long cached data remains valid.

Example:

Cache created at 10:00
TTL = 60 seconds
Expires around 10:01

Basic Cache Concept

cache = {}

cache[key] = {
    "data": result,
    "expires_at": timestamp
}

On request:

Cache exists?
   ↓
Yes
   ↓
Expired?
 ┌─┴─┐
No  Yes
 ↓    ↓
Return  Recompute

Cache Hit vs Cache Miss

Cache Hit
→ Data found and still valid

Cache Miss
→ Data unavailable/expired, perform original operation

Why Cache?

Can reduce:

Latency

External API calls

Database load

Repeated computation

29. Rate Limiting

Concepts Covered

What is Rate Limiting?

Why Rate Limit?

429

SlowAPI

Flow

What is Rate Limiting?

Rate limiting restricts how many requests a client can make within a
given time period.

Example:

5 requests / minute

The sixth request may be rejected.

Why Rate Limit?

Prevent abuse

Reduce spam

Protect server resources

Protect expensive endpoints

Reduce brute-force attempts

Control traffic

429

The standard status code for too many requests is:

429 Too Many Requests

SlowAPI

The course uses:

SlowAPI

with:

get_remote_address

to identify clients by remote address.

Concept:

@limiter.limit("5/minute")
async def endpoint(...):
    ...

Flow

Request
 ↓
Identify Client
 ↓
Count Requests
 ↓
Limit Exceeded?
 ┌───────┴───────┐
No              Yes
 ↓                ↓
Process          429

30. Deployment on Render

Concepts Covered

Local vs Production

requirements.txt

GitHub

Render Start Command

Deployment Checklist

Local vs Production

Local:

127.0.0.1:8000

Production:

Internet
   ↓
Cloud Platform
   ↓
FastAPI Application

requirements.txt

Create dependency file:

pip freeze > requirements.txt

Install dependencies:

pip install -r requirements.txt

GitHub

Typical flow:

Local Project
    ↓
Git
    ↓
GitHub Repository
    ↓
Render
    ↓
Build + Deploy

Render Start Command

The course uses:

uvicorn main:app --host 0.0.0.0 --port 10000

Why 0.0.0.0?

It allows the application to listen on all network interfaces inside the
deployment environment.

Why Port?

The deployment environment expects the application to listen on the
configured service port.

Deployment Checklist

[ ] Code works locally
[ ] requirements.txt exists
[ ] .env secrets are not committed
[ ] GitHub repository is ready
[ ] Start command is correct
[ ] Database configuration is correct
[ ] CORS is configured
[ ] Production environment variables are set

31. Capstone --- Complete PostgreSQL Blog API

This final project combines the major concepts from the course.

Concepts Covered

Project

Features

Part 1 --- PostgreSQL Setup

Part 2 --- Blog CRUD

Part 3 --- JWT Security

Part 4 --- Search & Pagination

Part 5 --- GitHub / Production

Path vs Query vs Body

PUT vs PATCH

Authentication vs Authorization

Project

PostgreSQL Blog API

Features

├── PostgreSQL
├── SQLAlchemy
├── Pydantic
├── CRUD
├── JWT Authentication
├── OAuth2 Password Bearer
├── Protected Routes
├── Search
├── Pagination
├── Testing
└── Deployment

Part 1 --- PostgreSQL Setup

Create database:

blog_db

The course uses PostgreSQL connectivity through:

psycopg2-binary

Database can be created/managed using PostgreSQL tools such as pgAdmin
or terminal.

Typical architecture:

FastAPI
   ↓
SQLAlchemy
   ↓
psycopg2
   ↓
PostgreSQL

Part 2 --- Blog CRUD

Blog Model

Typical fields:

id
title
content

SQLAlchemy model concept:

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

Create Blog

POST /blogs

Request:

{
  "title": "FastAPI",
  "content": "Learning FastAPI"
}

Flow:

Request
 ↓
Pydantic
 ↓
SQLAlchemy Model
 ↓
db.add()
 ↓
db.commit()
 ↓
db.refresh()
 ↓
Response

Read All

GET /blogs

Read One

GET /blogs/{blog_id}

Update

PUT /blogs/{blog_id}

Delete

DELETE /blogs/{blog_id}

Part 3 --- JWT Security

Some blog operations can be protected.

Example:

GET  /blogs       → public
POST /blogs       → authenticated
PUT  /blogs/{id}  → authenticated
DELETE /blogs/{id} → authenticated

Authentication flow:

Login
 ↓
Verify credentials
 ↓
Generate JWT
 ↓
Bearer token
 ↓
Dependency
 ↓
Verify JWT
 ↓
Allow protected operation

Part 4 --- Search & Pagination

Search example:

GET /blogs?search=fastapi

Case-insensitive title search can be used to find matching blog posts.

Pagination:

GET /blogs?page=2&limit=10

Combined:

GET /blogs?search=fastapi&page=2&limit=10

Flow:

Request
 ↓
Search Filter
 ↓
Pagination
 ↓
PostgreSQL
 ↓
Response

Part 5 --- GitHub / Production

Final project should be pushed to GitHub.

Typical workflow:

git add .
git save -m "Complete PostgreSQL Blog API"
git push

If your Git setup uses the save alias, use git save as above.

🔥 Complete FastAPI Architecture

                         CLIENT
                           │
                           ▼
                        HTTP
                           │
                           ▼
                      MIDDLEWARE
                           │
                           ▼
                       ROUTER
                           │
              ┌────────────┼────────────┐
              │            │            │
             PATH         QUERY        BODY
              │            │            │
              └────────────┼────────────┘
                           ▼
                    PYDANTIC VALIDATION
                           │
                           ▼
                    DEPENDENCY INJECTION
                           │
                  ┌────────┴────────┐
                  │                 │
                AUTH              DB
                JWT             SESSION
                  │                 │
                  └────────┬────────┘
                           ▼
                    BUSINESS LOGIC
                           │
                           ▼
                       SQLALCHEMY
                           │
                           ▼
                       POSTGRESQL
                           │
                           ▼
                    RESPONSE MODEL
                           │
                           ▼
                         JSON
                           │
                           ▼
                        CLIENT

🧠 Complete Request Lifecycle

1. Client sends HTTP request
        ↓
2. Middleware receives request
        ↓
3. FastAPI matches route
        ↓
4. Path/query/body parameters are extracted
        ↓
5. Pydantic validates request data
        ↓
6. Dependencies are resolved
        ↓
7. Authentication/authorization is checked
        ↓
8. Route function executes
        ↓
9. Business logic runs
        ↓
10. Database/external API is accessed
        ↓
11. Response model validates/filters output
        ↓
12. JSON response is returned
        ↓
13. Middleware can process response
        ↓
14. Client receives response

🔐 Complete Authentication Lifecycle

REGISTER
   ↓
Email + Password
   ↓
Pydantic Validation
   ↓
Hash Password
   ↓
Save User
   ↓
PostgreSQL

LOGIN
   ↓
Email + Password
   ↓
Find User
   ↓
Verify Password Hash
   ↓
Generate JWT
   ↓
Return Access Token

PROTECTED REQUEST
   ↓
Authorization: Bearer <JWT>
   ↓
Dependency
   ↓
Decode JWT
   ↓
Verify Signature
   ↓
Check Expiration
   ↓
Identify User
   ↓
Authorization Check
   ↓
Endpoint

🗄️ Complete Database Lifecycle

FastAPI Request
      ↓
Pydantic
      ↓
Route
      ↓
Depends(get_db)
      ↓
SessionLocal
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
Query / Insert / Update / Delete
      ↓
Commit
      ↓
Refresh
      ↓
Response Model

📌 Most Important Differences

Path vs Query vs Body

Feature          Path                Query             Body

Example          /users/10         /users?page=2   JSON payload
Main use         Identify resource   Filter/control    Send structured data
Common methods   GET/PUT/DELETE      GET               POST/PUT/PATCH

PUT vs PATCH

PUT
→ Complete replacement/update

PATCH
→ Partial update

Authentication vs Authorization

Authentication
→ Who are you?

Authorization
→ What can you do?

Hashing vs Encryption

Hashing
→ One-way

Encryption
→ Reversible with key

Middleware vs Dependency

Middleware
→ Global request/response layer

Dependency
→ Reusable injected logic/resource

Pydantic vs SQLAlchemy

Pydantic
→ API input/output validation

SQLAlchemy
→ Database mapping + database operations

FastAPI vs Uvicorn

FastAPI
→ Web framework

Uvicorn
→ ASGI server that runs the application

SQLite vs PostgreSQL

SQLite
→ Lightweight file-based DB

PostgreSQL
→ Full relational database server

⚡ One-Line Definitions

Concept                             Definition

API                                 Interface through which software
components communicate

Backend                             Server-side application logic and
services

FastAPI                             Python framework for building APIs

Route                               URL path mapped to application
logic

Endpoint                            Specific API operation exposed to
clients

HTTP                                Protocol used for web communication

GET                                 HTTP method for retrieving
resources

POST                                HTTP method commonly used to create
resources

PUT                                 HTTP method commonly used for
complete replacement

PATCH                               HTTP method for partial updates

DELETE                              HTTP method for deleting resources

Path Parameter                      Dynamic value embedded in a URL
path

Query Parameter                     Key-value data after ? in a URL

Request Body                        Structured data sent inside an HTTP
request

Pydantic                            Library for validation/parsing
structured data

BaseModel                           Pydantic base class for schemas

Response Model                      Schema defining/sanitizing API
output

CRUD                                Create, Read, Update, Delete

HTTPException                       FastAPI mechanism for raising HTTP
errors

Exception Handler                   Function that converts exceptions
into responses

Dependency Injection                Providing required reusable
resources/logic automatically

Depends                             FastAPI helper for dependency
injection

Middleware                          Layer around request/response
processing

ORM                                 Object Relational Mapping

SQLAlchemy                          Python SQL toolkit and ORM

Engine                              SQLAlchemy database connectivity
infrastructure

Session                             SQLAlchemy interface for DB
operations

SQLite                              Lightweight file-based relational
database

PostgreSQL                          Powerful relational database system

Async                               Programming model for non-blocking
I/O

async def                         Defines an asynchronous coroutine
function

await                             Waits for an async operation
without blocking the event loop

JWT                                 Signed token format commonly used
for authentication

Authentication                      Verification of user identity

Authorization                       Verification of permissions

OAuth2                              Authorization framework used by
many authentication flows

Bearer Token                        Token sent through Authorization
header

Hashing                             One-way transformation used for
secure password storage

CORS                                Browser mechanism controlling
cross-origin access

UploadFile                          FastAPI type for uploaded files

Static Files                        Files served directly from a
directory

.env                              File commonly used for local
environment configuration

PyTest                              Python testing framework

TestClient                          Client used to test FastAPI
endpoints

Third-Party API                     External API provided by another
service

Web Scraping                        Programmatically extracting
information from web pages

Pagination                          Dividing a large dataset into
smaller pages

Cache                               Temporary storage for faster
repeated access

TTL                                 Time To Live; cache expiration
duration

Rate Limiting                       Restricting request frequency

429                                 Too Many Requests

Uvicorn                             ASGI server

ASGI                                Interface between async Python web
apps and servers

OpenAPI                             Standard specification for
describing APIs

Swagger UI                          Interactive API documentation

ReDoc                               API documentation interface

🎯 FastAPI Cheat Sheet

Start Project

python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn

uvicorn main:app --reload

Generate Requirements

pip freeze > requirements.txt

Install Requirements

pip install -r requirements.txt

Docs

/docs
/redoc

Basic Route

@app.get("/")
def home():
    return {"message": "Hello"}

Path Parameter

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"id": user_id}

Query Parameter

@app.get("/users")
def get_users(limit: int = 10):
    return {"limit": limit}

Request Body

class User(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: User):
    return user

Response Model

@app.get(
    "/users/{id}",
    response_model=UserResponse
)
def get_user(id: int):
    ...

HTTPException

raise HTTPException(
    status_code=404,
    detail="Not found"
)

Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db: Session = Depends(get_db)

Middleware

@app.middleware("http")
async def middleware(request, call_next):
    response = await call_next(request)
    return response

JWT Header

Authorization: Bearer <token>

CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

🧩 Important Packages

The course uses or introduces packages/tools including:

fastapi
uvicorn
pydantic
sqlalchemy
sqlite3
psycopg2-binary
python-jose
passlib[bcrypt]
python-dotenv
pytest
requests
beautifulsoup4
slowapi

Typical roles:

Package                    Purpose

fastapi                    API framework
uvicorn                    ASGI server
pydantic                   Data validation
sqlalchemy                 ORM/database toolkit
sqlite3                    SQLite access
psycopg2-binary            PostgreSQL driver
python-jose                JWT handling
passlibbcrypt   Password hashing
python-dotenv              .env loading
pytest                     Testing
requests                   HTTP requests
beautifulsoup4             HTML parsing
slowapi                    Rate limiting

🛠️ Production Checklist

Before considering a FastAPI backend production-ready:

API

Correct HTTP methods

Correct status codes

Input validation

Response models

Proper error handling

Database

PostgreSQL/appropriate production DB

SQLAlchemy models

Session cleanup

Transactions

Indexes where required

Security

Password hashing

JWT expiration

Secrets in environment variables

Protected routes

Authorization checks

CORS configured correctly

Rate limiting where required

Performance

Pagination

Caching where useful

Efficient database queries

Async for suitable I/O workloads

Avoid unnecessary external requests

Testing

Unit tests

API tests

Authentication tests

Error cases

Edge cases

Deployment

requirements.txt

GitHub repository

Environment variables

Correct start command

Production database

Logs/monitoring

🧠 10-Minute Revision

If you have very little time, remember this:

1. FastAPI
   → Python API framework

2. Route
   → Method + path mapped to function

3. Path Parameter
   → /users/{id}

4. Query Parameter
   → /users?page=2

5. Body
   → JSON data sent by client

6. Pydantic
   → Validate/parse request & response data

7. CRUD
   → Create Read Update Delete

8. Response Model
   → Control API output

9. HTTPException
   → Proper API error

10. Depends
    → Dependency Injection

11. Middleware
    → Global request/response layer

12. SQLAlchemy
    → ORM/database toolkit

13. Session
    → DB operations

14. async/await
    → Async I/O/concurrency

15. JWT
    → Signed authentication token

16. OAuth2
    → Authorization/security flow

17. Password Hashing
    → Never store plain passwords

18. CORS
    → Browser cross-origin control

19. PyTest
    → Testing

20. Pagination
    → Split large datasets

21. Cache
    → Reuse expensive results

22. Rate Limit
    → Control request frequency

23. PostgreSQL
    → Production relational DB

24. Deployment
    → Run API on cloud/server

🔥 Final Mental Model

The whole FastAPI course can be reduced to this:

                    CLIENT
                       │
                       ▼
                  HTTP REQUEST
                       │
                       ▼
                   FASTAPI
                       │
             ┌─────────┴─────────┐
             │                   │
         Middleware           Routing
             │                   │
             └─────────┬─────────┘
                       ▼
              PATH / QUERY / BODY
                       │
                       ▼
                  PYDANTIC
                  VALIDATION
                       │
                       ▼
                DEPENDENCIES
                       │
             ┌─────────┴─────────┐
             │                   │
          AUTH/JWT             DB
             │                 SESSION
             │                   │
             └─────────┬─────────┘
                       ▼
                  ENDPOINT
                       │
                       ▼
                BUSINESS LOGIC
                       │
                       ▼
                  SQLALCHEMY
                       │
                       ▼
                  POSTGRESQL
                       │
                       ▼
                RESPONSE MODEL
                       │
                       ▼
                     JSON
                       │
                       ▼
                    CLIENT

🏆 Final Revision Checklist

Fundamentals

Backend

API

Client-server architecture

HTTP

JSON

HTTP methods

FastAPI

FastAPI app

Routes

Endpoints

Uvicorn

ASGI

Swagger

ReDoc

OpenAPI

Parameters

Path parameters

Query parameters

Request body

Multiple parameters

Pydantic

BaseModel

Type validation

Nested models

Request schemas

Response schemas

CRUD

Create

Read all

Read one

Update

Delete

PUT vs PATCH

Postman

Thunder Client

Errors

HTTP status codes

HTTPException

Custom exceptions

Global exception handlers

Architecture

Dependency Injection

Depends

Middleware

call_next

Middleware vs Dependency

Database

SQLite

sqlite3

ORM

Raw SQL vs ORM

SQLAlchemy

Engine

Session

get_db

Models

PostgreSQL

psycopg2-binary

Async

Sync

Async

async def

await

asyncio

I/O-bound workloads

Security

Authentication

Authorization

JWT

Header

Payload

Signature

Expiration

python-jose

Password hashing

bcrypt

OAuth2

Bearer token

Protected routes

Files & Frontend

UploadFile

File

Multipart upload

Static files

app.mount

CORS

CORSMiddleware

React + FastAPI integration

Configuration

.env

python-dotenv

Settings/config

.gitignore

Secret management

Testing

PyTest

TestClient

Assertions

Status code tests

JSON response tests

External Services

requests

Third-party APIs

Error handling

BeautifulSoup4

HTML parsing

Scraping considerations

Performance

Pagination

Offset

Limit

Search

Cache

TTL

Cache hit/miss

Rate limiting

SlowAPI

429

Deployment

requirements.txt

GitHub

Render

Environment variables

Uvicorn start command

0.0.0.0

Production configuration

Capstone

PostgreSQL setup

blog_db

Blog model

Pydantic schemas

Blog CRUD

JWT security

OAuth2

Protected routes

Search

Pagination

GitHub push

Deployment

🚀 What You Should Be Able To Build After This Course

After completing this course, the target is to be able to independently
build a backend like:

React / Frontend
       │
       ▼
    FastAPI
       │
 ┌─────┼─────────────┐
 │     │             │
Auth  CRUD       External APIs
 │     │             │
JWT   SQLAlchemy    requests
 │     │             │
 └─────┼─────────────┘
       │
   PostgreSQL
       │
 ┌─────┼─────────────┐
 │     │             │
Cache Pagination Rate Limit
 │     │             │
 └─────┼─────────────┘
       │
    Testing
       │
       ▼
   Deployment

Final Principle

FastAPI mastery is not about memorizing syntax.

It is about understanding:

Request
   ↓
Validation
   ↓
Dependencies
   ↓
Authentication
   ↓
Business Logic
   ↓
Database / External API
   ↓
Response
   ↓
Testing
   ↓
Deployment

If you understand this complete flow, you understand the core
architecture behind a real FastAPI backend.