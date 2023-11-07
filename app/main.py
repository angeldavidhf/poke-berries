from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI()
app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    import os

    app_port = os.getenv("APP_PORT")
    app_host = os.getenv("APP_HOST")
    uvicorn.run(app, host=f"{app_host}", port=int(app_port))
