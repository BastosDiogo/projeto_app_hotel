from models.quartos import Quartos
from base_model.quarto_model import QuartoModel

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import admin
from routes import user


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router)
app.include_router(user.router)