from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    "mysql+pymysql://root:@localhost/airport_intelligence"
)

REPORTS_DIR = Path("sql/reports")

reports = {
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

for report_name, file_name in reports.items():
    query_path = REPORTS_DIR / file_name
    query = query_path.read_text()

    df = pd.read_sql(query, engine)

    print("\n" + "=" * 60)
    print(report_name)
    print("=" * 60)
    print(df.head(10))