from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.config import settings
from app.routes import users

# app = FastAPI()


MONGO_URI = settings.MONGO_URI
MONGO_DB = settings.MONGO_DB


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        print("Connecting to MongoDB...")

        mongo_client = AsyncIOMotorClient(MONGO_URI)
        await mongo_client.admin.command("ping")  # Check DB connection
        print("✅ Successfully connected to MongoDB!")

        app.state.mongo_client = mongo_client
        app.state.mongo_db = mongo_client[MONGO_DB]

        yield  # Run app

    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        raise e  # Fail fast if DB is critical

    finally:
        mongo_client.close()
        print("❌ Disconnected from MongoDB")


# ⬇ Register lifespan here
app = FastAPI(lifespan=lifespan)

routers = [
    (users.router, "/api/users"),
]


for router, prefix in routers:
    print(f"Registering router with prefix: {prefix}")
    app.include_router(router, prefix=prefix)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"error": "The page you were looking for does not exist."},
        )
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


if __name__ == "__main__":
    port = settings.PORT

    uvicorn.run("main:app", host="127.0.0.1", port=port, reload=True)
