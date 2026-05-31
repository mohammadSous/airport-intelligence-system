'''Create API
Connect report routes
Create homepage'''
from fastapi import FastAPI
from api.routes import reports, summary, flights, airlines, predictions
#creates the api app
app = FastAPI(
    title="Airport Intelligence API",
    description="API for airport analytics reports, dashboard data, and future ML predictions.",
    version="1.0.0"
)

#attaches the endpoints from reports.py to the main api app 
app.include_router(reports.router)
app.include_router(summary.router)
app.include_router(flights.router)
app.include_router(airlines.router)
app.include_router(predictions.router)

#create the homepage route
@app.get("/")
def home():
    return {
        "message": "Airport Intelligence API is running",
        "docs": "/docs",
        "reports": "/api/reports",
        "summary": "/api/summary",
        "flights": "/api/flights",
        "airlines": "/api/airlines",
        "predictions": "/api/predictions/delay"
    }