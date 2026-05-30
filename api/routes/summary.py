from fastapi import APIRouter
from utils.load_queries import load_report

router = APIRouter(
    prefix="/api/summary",
    tags=["summary"]
)

@router.get("/")
def get_summary():
    flights_df = load_report("Flights per airline")
    delays_df = load_report("Delayed flights per airline")
    revenue_df = load_report("Total revenue per airline")

    total_flights = int(flights_df["total_flights"].sum())
    total_delayed_flights = int(delays_df["delayed_flights"].sum())
    total_revenue = float(revenue_df["total_revenue"].sum())
    number_of_airlines = int(len(flights_df))

    delay_rate = round((total_delayed_flights / total_flights) * 100, 2)

    return {
        "total_flights": total_flights,
        "total_delayed_flights": total_delayed_flights,
        "total_revenue": total_revenue,
        "number_of_airlines": number_of_airlines,
        "delay_rate": delay_rate
    }