from fastapi import FastAPI, Depends
from datetime import datetime
import pytz
from os import path
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi_health import health

app = FastAPI()

@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

def moscow_time():
    timezone = pytz.timezone('Europe/Moscow')

    return datetime.now(timezone).isoformat()
@app.get("/")
async def root():
    time = moscow_time()
    await write_time(time)
    return {"time": f"{time}"}

@app.get("/visits")
async def get_visits():
    with open("./data/visits.txt", "r+") as file:
        return file.read()

async def write_time(time):
    with open("./data/visits.txt", "a+") as file:
        file.write(f"{{ \"time\": \"{time}\"}}\n")

def get_session():
    return True

def is_app_online(session: bool = Depends(get_session)):
    return session

app.add_api_route("/health", health([is_app_online]))
