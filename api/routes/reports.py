import json

from fastapi import APIRouter, HTTPException #mini route manager, and API error.
from utils.load_queries import CHARTS, load_report

#every route in this file starts with /api/reports (for the URL)
router = APIRouter(
    prefix="/api/reports",
    tags=["Reports"]
)

#a cleaner format to write URLS for the report names.
REPORT_ENDPOINTS = {
    "flights-per-airline": "Flights per airline",
    "delayed-flights-per-airline": "Delayed flights per airline",
    "average-ticket-price-per-airline": "Average ticket price per airline",
    "total-revenue-per-airline": "Total revenue per airline",
    "most-popular-destinations": "Most popular destinations",
    "tickets-sold-per-flight": "Tickets sold per flight",
    "baggage-count-per-passenger": "Baggage count per passenger",
    "average-baggage-weight-by-type": "Average baggage weight by type",
    "employee-flight-assignment-count": "Employee flight assignment count",
    "flights-by-status": "Flights by status",
}


def dataframe_to_records(df):
    """
    Convert a Pandas DataFrame into JSON-friendly records.
    """
    return json.loads(
        df.to_json(
            orient="records",
            date_format="iso"
        )
    )

#returns a URL /api/repots/{/report_id}
@router.get("/")
def list_reports():
    """
    Return all available report endpoints.
    """
    reports = []

    for report_id, report_name in REPORT_ENDPOINTS.items():
        reports.append({
            "report_id": report_id,
            "report_name": report_name,
            "url": f"/api/reports/{report_id}"
        })

    return reports


@router.get("/{report_id}")
def get_report(report_id: str):
    """
    Return a full SQL report as JSON.
    """
    if report_id not in REPORT_ENDPOINTS:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report_name = REPORT_ENDPOINTS[report_id]
    df = load_report(report_name)

    return {
        "report_id": report_id,
        "report_name": report_name,
        "row_count": len(df),
        "data": dataframe_to_records(df)
    }


@router.get("/{report_id}/preview")
def preview_report(report_id: str, limit: int = 10):
    """
    Return only the first rows of a report.
    """
    if report_id not in REPORT_ENDPOINTS:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report_name = REPORT_ENDPOINTS[report_id]
    df = load_report(report_name).head(limit)

    return {
        "report_id": report_id,
        "report_name": report_name,
        "preview_limit": limit,
        "data": dataframe_to_records(df)
    }