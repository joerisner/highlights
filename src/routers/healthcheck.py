from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/health")


class HealthCheck(BaseModel):
    status: str = "UP"


@router.get("")
def get_health() -> HealthCheck:
    """
    Perform a health check of the application.
    """
    return HealthCheck()
