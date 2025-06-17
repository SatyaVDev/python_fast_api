import uvicorn
from fastapi import FastAPI ,Request


from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager


from app.routes import users
from app.config import settings


app = FastAPI()


MONGO_URI =settings.MONGO_URI
MONGO_DB = settings.MONGO_DB

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("___________________>", MONGO_URI)

    mongo_client = AsyncIOMotorClient(MONGO_URI)
    app.state.mongo_client = mongo_client
    app.state.mongo_db = mongo_client[MONGO_DB]
    print("✅ Connected to MongoDB")

    yield  # Run the app

    # Shutdown
    mongo_client.close()
    print("❌ Disconnected from MongoDB")


routers = [
    (users.router, "/api/users"),
]


for router, prefix in routers:
    print(f"Registering router with prefix: {prefix}")
    app.include_router(router, prefix=prefix)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!ww"}


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
