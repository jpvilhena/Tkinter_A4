"""
MudaExpress FastAPI Application Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import (
    router_cliente,
    router_caminhao,
    router_prestador,
    router_servico,
    router_contrato,
    router_alocacao,
    router_contrato_prestador,
)

app = FastAPI(
    title="MudaExpress API",
    description="Backend for MudaExpress moving service management",
    version="0.0.7",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_cliente)
app.include_router(router_caminhao)
app.include_router(router_prestador)
app.include_router(router_servico)
app.include_router(router_contrato)
app.include_router(router_alocacao)
app.include_router(router_contrato_prestador)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}