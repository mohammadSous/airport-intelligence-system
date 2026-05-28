import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:@localhost/airport_intelligence"
)

REPORTS_DIR = Path("sql/reports")

reports = {
    "Flights per airline": "flights_per_airline.sql",
    "Total revenue per airline": "total_revenue_per_airline.sql",
    "Most popular destinations": "most_popular_destinations.sql",
    "Average baggage weight by type": "average_baggage_weight_by_type.sql",
    "Employee flight assignment count": "employee_flight_assignment_count.sql",
    "Flights by status": "flights_by_status.sql",
}

result = {}

for report_name, file_name in reports.items():
    query_path = REPORTS_DIR / file_name
    query = query_path.read_text()
    df = pd.read_sql(query,engine)
    result[report_name] = df

charts = {
    "Flights per airline": ("airline", "total_flights"),
    "Total revenue per airline": ("airline", "total_revenue"),
    "Most popular destinations": ("destination", "total_flights"),
    "Average baggage weight by type": ("baggage_type", "average_weight"),
    "Employee flight assignment count": ("employee_name", "flights_assigned"),
    "Flights by status": ("status", "flight_count"),
}

for report_name, (x_col, y_col) in charts.items():
    df = result[report_name]

    plt.figure(figsize=(10, 5))
    plt.bar(df[x_col], df[y_col])
    plt.title(report_name)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()