from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import models
from api.database import engine
from api.middleware.middleware import AdminMiddleware
from api.router import api_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = [
    "http://localhost:3000",
]

app.add_middleware(AdminMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
