from fastapi import FastAPI, Depends
from redis import Redis

app = FastAPI()

redis = Redis(host='redis', port=6379, db=0)

@app.get("/")
def read_root():
    cached_data = redis.get("cached_data")
    if cached_data:
        return {"data": cached_data.decode('utf-8')}
    else:
        data = "Hello, World!"
        redis.set("cached_data", data)
        return {"data": data}
