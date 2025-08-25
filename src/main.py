from fastapi import FastAPI, Response

from .routers.authors import router as authors_router
from .routers.health import router as healthcheck_router

app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(authors_router)


@app.get("/")
def get_root() -> Response:
    return Response("Application is running.")
