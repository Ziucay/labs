from prometheus_fastapi_instrumentator import Instrumentator
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

# Expose /metrics endpoint for prometheus
@app.on_event("startup")
async def startup():
    Instrumentator().instrument(app).expose(app)

def moscow_time():
    timezone = pytz.timezone('Europe/Moscow')

    return datetime.now(timezone).isoformat()
@app.get("/")
async def root():
    return {"time": f"{moscow_time()}"}
