import uvicorn
from fastapi import FastAPI

app = FastAPI()
from app.routes import users

routers = [
    (users.router, "/api/users"),
]


for router, prefix in routers:
    app.include_router(router, prefix=prefix)


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!ww"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8081, reload=True)
