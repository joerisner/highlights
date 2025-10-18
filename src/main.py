from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .routers.authors import router as authors_router
from .routers.health import router as healthcheck_router
from .routers.highlights import router as highlights_router
from .routers.sources import router as sources_router
from .routers.tags import router as tags_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.include_router(healthcheck_router)
app.include_router(authors_router)
app.include_router(highlights_router)
app.include_router(sources_router)
app.include_router(tags_router)


@app.get("/")
def get_root() -> JSONResponse:
    return JSONResponse(content={"message": "Application is running."})
