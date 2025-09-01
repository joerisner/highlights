from fastapi import FastAPI, Response

from .routers.authors import router as authors_router
from .routers.health import router as healthcheck_router
from .routers.sources import router as sources_router
from .routers.tags import router as tags_router

app = FastAPI()

app.include_router(healthcheck_router)
app.include_router(authors_router)
app.include_router(sources_router)
app.include_router(tags_router)


@app.get("/")
def get_root() -> Response:
    return {"message": "Application is running."}
