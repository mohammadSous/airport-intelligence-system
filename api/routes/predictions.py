from fastapi import APIRouter
from pydantic import BaseModel

from ml.predict import predict_delay


router = APIRouter(
    prefix="/api/predictions",
    tags=["predictions"]
)


class DelayPredictionInput(BaseModel):
    airline: str
    origin: str
    destination: str
    gate_id: str
    departure_hour: int
    departure_day_of_week: int
    tickets_sold: int
    average_ticket_price: float
    employee_count: int
    baggage_count: int
    total_baggage_weight: float


@router.post("/delay")
def predict_flight_delay(flight: DelayPredictionInput):
    flight_data = flight.model_dump()

    result = predict_delay(flight_data)

    return result