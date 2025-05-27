from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
#from app.api import router as api_router
from app.api.router import router as api_router
from app.core.config import settings
from app.db.base_class import Base
from app.db.session import engine

app = FastAPI(
    title="API Availability Monitoring SaaS",
    version="1.0.0"
)

app = FastAPI()

#@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)