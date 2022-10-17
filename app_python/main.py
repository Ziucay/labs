from starlette_exporter import PrometheusMiddleware, handle_metrics
from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

# Expose /metrics endpoint for prometheus
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

def moscow_time():
    timezone = pytz.timezone('Europe/Moscow')

    return datetime.now(timezone).isoformat()
@app.get("/")
async def root():
    return {"time": f"{moscow_time()}"}
