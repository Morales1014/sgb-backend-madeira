from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.presentation.controller import router as recurso_router

app = FastAPI(title="SGB Universidad de Madeira API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recurso_router)