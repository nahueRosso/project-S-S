from fastapi import FastAPI

from app.routers.health import router as health_router
from app.settings import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API REST para generacion, procesamiento y analisis de RIR.",
)

app.include_router(health_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "RIR API",
        "docs": "/docs",
        "health": "/health",
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
