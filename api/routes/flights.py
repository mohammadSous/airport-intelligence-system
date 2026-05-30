from utils.helpers import dataframe_to_records
from fastapi import APIRouter, HTTPException #mini route manager, and API error.
from utils.load_queries import load_report, FLIGHT_REPORTS

router = APIRouter(
    prefix="/api/flights",
    tags=["flights"]
)

@router.get("/")
def list_reports():
    """
    Return all available report endpoints.
    """
    reports = []

    for report_id, report_name in FLIGHT_REPORTS.items():
        reports.append({
            "report_id": report_id,
            "report_name": report_name,
            "url": f"/api/flights/{report_id}"
        })

    return reports


@router.get("/{report_id}")
def get_report(report_id: str):
    """
    Return a full SQL report as JSON.
    """
    if report_id not in FLIGHT_REPORTS:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report_name = FLIGHT_REPORTS[report_id]
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
    if report_id not in FLIGHT_REPORTS:
        raise HTTPException(
            status_code=404,
            detail="Report not found"
        )

    report_name = FLIGHT_REPORTS[report_id]
    df = load_report(report_name).head(limit)

    return {
        "report_id": report_id,
        "report_name": report_name,
        "preview_limit": limit,
        "data": dataframe_to_records(df)
    }