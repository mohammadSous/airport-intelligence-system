from pathlib import Path
import pandas as pd
from utils.db_connection import get_engine

REPORTS_DIR = Path("sql/reports")

REPORTS = {
    "Flights per airline": "flights_per_airline.sql",
    "Delayed flights per airline": "delayed_flights_per_airline.sql",
    "Average ticket price per airline": "average_ticket_price_per_airline.sql",
    "Total revenue per airline": "total_revenue_per_airline.sql",
    "Most popular destinations": "most_popular_destinations.sql",
    "Tickets sold per flight": "tickets_sold_per_flight.sql",
    "Baggage count per passenger": "baggage_count_per_passenger.sql",
    "Average baggage weight by type": "average_baggage_weight_by_type.sql",
    "Employee flight assignment count": "employee_flight_assignment_count.sql",
    "Flights by status": "flights_by_status.sql",
}

CHARTS = {
    "Flights per airline": ("airline", "total_flights"),
    "Delayed flights per airline": ("airline", "delayed_flights"),
    "Average ticket price per airline": ("airline", "average_ticket_price"),
    "Total revenue per airline": ("airline", "total_revenue"),
    "Most popular destinations": ("destination", "total_flights"),
    "Tickets sold per flight": ("flight_id", "tickets_sold"),
    "Baggage count per passenger": ("passenger_id", "baggage_count"),
    "Average baggage weight by type": ("baggage_type", "average_weight"),
    "Employee flight assignment count": ("employee_name", "flights_assigned"),
    "Flights by status": ("status", "flight_count"),
}
CHARTS_TO_SHOW = {
    "Flights per airline": CHARTS["Flights per airline"],
    "Total revenue per airline": CHARTS["Total revenue per airline"],
    "Most popular destinations": CHARTS["Most popular destinations"],
    "Average baggage weight by type": CHARTS["Average baggage weight by type"],
    "Employee flight assignment count": CHARTS["Employee flight assignment count"],
    "Flights by status": CHARTS["Flights by status"],
}

def load_report(report_name):
    engine = get_engine()

    file_name = REPORTS[report_name]
    query_path = REPORTS_DIR / file_name
    query = query_path.read_text()

    df = pd.read_sql(query, engine)
    return df