from fastapi import FastAPI, Depends
from datetime import datetime
import pytz
import json
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
    if not path.exists('data/visits.json'):
        with open('visits.json', 'w') as f:
            pass
    f = open('data/visits.json')

    data = json.load(f)

    return json.dumps(data)

async def write_time(time):
    with open("data/visits.json", "a") as file:
        file.write(f"{{ \"time\": \"{time}\"}}\n")

def get_session():
    return True

def is_app_online(session: bool = Depends(get_session)):
    return session

app.add_api_route("/health", health([is_app_online]))
