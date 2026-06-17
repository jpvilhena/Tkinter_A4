"""
FastAPI Routers — Full CRUD for all MudaExpress entities.

Each router provides:
  GET    /           → list all (with optional pagination)
  GET    /{id}       → get one by ID
  POST   /           → create
  PATCH  /{id}       → partial update
  DELETE /{id}       → delete

Mount in main.py with app.include_router(...).
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from .database import get_db
from .models import (
    Cliente,
    Caminhao,
    Prestador,
    ServicoOferecido,
    ContratoMudanca,
    AlocacaoServico,
    ContratoPrestador,
)
from .schemas import (
    ClienteCreate, ClienteUpdate, ClienteResponse,
    CaminhaoCreate, CaminhaoUpdate, CaminhaoResponse,
    PrestadorCreate, PrestadorUpdate, PrestadorResponse,
    ServicoOferecidoCreate, ServicoOferecidoUpdate, ServicoOferecidoResponse,
    ContratoMudancaCreate, ContratoMudancaUpdate, ContratoMudancaResponse,
    AlocacaoServicoCreate, AlocacaoServicoUpdate, AlocacaoServicoResponse,
    ContratoPrestadorCreate, ContratoPrestadorUpdate, ContratoPrestadorResponse,
)


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def get_or_404(db: Session, model, record_id: int):
    """Fetch a record by primary key or raise 404."""
    obj = db.get(model, record_id)
    if obj is None:
        raise HTTPException(status_code=404, detail=f"{model.__name__} not found")
    return obj


def apply_patch(obj, data):
    """Apply only the non-None fields from a Pydantic update schema onto an ORM object."""
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(obj, field, value)
    return obj


def safe_commit(db: Session):
    """Commit and raise 409 on integrity violations (e.g. duplicate CPF)."""
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(status_code=409, detail=f"Integrity error: {exc.orig}")


# ─────────────────────────────────────────────
# Cliente
# ─────────────────────────────────────────────

router_cliente = APIRouter(prefix="/clientes", tags=["Clientes"])


@router_cliente.get("/", response_model=List[ClienteResponse])
def list_clientes(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(Cliente).offset(skip).limit(limit).all()


@router_cliente.get("/{id_cliente}", response_model=ClienteResponse)
def get_cliente(id_cliente: int, db: Session = Depends(get_db)):
    return get_or_404(db, Cliente, id_cliente)


@router_cliente.post("/", response_model=ClienteResponse, status_code=201)
def create_cliente(payload: ClienteCreate, db: Session = Depends(get_db)):
    obj = Cliente(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_cliente.patch("/{id_cliente}", response_model=ClienteResponse)
def update_cliente(id_cliente: int, payload: ClienteUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, Cliente, id_cliente)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_cliente.delete("/{id_cliente}", status_code=204)
def delete_cliente(id_cliente: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, Cliente, id_cliente)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# Caminhao
# ─────────────────────────────────────────────

router_caminhao = APIRouter(prefix="/caminhoes", tags=["Caminhoes"])


@router_caminhao.get("/", response_model=List[CaminhaoResponse])
def list_caminhoes(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(Caminhao).offset(skip).limit(limit).all()


@router_caminhao.get("/{id_caminhao}", response_model=CaminhaoResponse)
def get_caminhao(id_caminhao: int, db: Session = Depends(get_db)):
    return get_or_404(db, Caminhao, id_caminhao)


@router_caminhao.post("/", response_model=CaminhaoResponse, status_code=201)
def create_caminhao(payload: CaminhaoCreate, db: Session = Depends(get_db)):
    obj = Caminhao(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_caminhao.patch("/{id_caminhao}", response_model=CaminhaoResponse)
def update_caminhao(id_caminhao: int, payload: CaminhaoUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, Caminhao, id_caminhao)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_caminhao.delete("/{id_caminhao}", status_code=204)
def delete_caminhao(id_caminhao: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, Caminhao, id_caminhao)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# Prestador
# ─────────────────────────────────────────────

router_prestador = APIRouter(prefix="/prestadores", tags=["Prestadores"])


@router_prestador.get("/", response_model=List[PrestadorResponse])
def list_prestadores(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(Prestador).offset(skip).limit(limit).all()


@router_prestador.get("/{id_prestador}", response_model=PrestadorResponse)
def get_prestador(id_prestador: int, db: Session = Depends(get_db)):
    return get_or_404(db, Prestador, id_prestador)


@router_prestador.post("/", response_model=PrestadorResponse, status_code=201)
def create_prestador(payload: PrestadorCreate, db: Session = Depends(get_db)):
    obj = Prestador(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_prestador.patch("/{id_prestador}", response_model=PrestadorResponse)
def update_prestador(id_prestador: int, payload: PrestadorUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, Prestador, id_prestador)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_prestador.delete("/{id_prestador}", status_code=204)
def delete_prestador(id_prestador: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, Prestador, id_prestador)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# ServicoOferecido
# ─────────────────────────────────────────────

router_servico = APIRouter(prefix="/servicos", tags=["Servicos"])


@router_servico.get("/", response_model=List[ServicoOferecidoResponse])
def list_servicos(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(ServicoOferecido).offset(skip).limit(limit).all()


@router_servico.get("/{id_servico}", response_model=ServicoOferecidoResponse)
def get_servico(id_servico: int, db: Session = Depends(get_db)):
    return get_or_404(db, ServicoOferecido, id_servico)


@router_servico.post("/", response_model=ServicoOferecidoResponse, status_code=201)
def create_servico(payload: ServicoOferecidoCreate, db: Session = Depends(get_db)):
    obj = ServicoOferecido(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_servico.patch("/{id_servico}", response_model=ServicoOferecidoResponse)
def update_servico(id_servico: int, payload: ServicoOferecidoUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, ServicoOferecido, id_servico)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_servico.delete("/{id_servico}", status_code=204)
def delete_servico(id_servico: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, ServicoOferecido, id_servico)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# ContratoMudanca
# ─────────────────────────────────────────────

router_contrato = APIRouter(prefix="/contratos", tags=["Contratos"])


@router_contrato.get("/", response_model=List[ContratoMudancaResponse])
def list_contratos(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(ContratoMudanca).offset(skip).limit(limit).all()


@router_contrato.get("/{id_contrato}", response_model=ContratoMudancaResponse)
def get_contrato(id_contrato: int, db: Session = Depends(get_db)):
    return get_or_404(db, ContratoMudanca, id_contrato)


@router_contrato.post("/", response_model=ContratoMudancaResponse, status_code=201)
def create_contrato(payload: ContratoMudancaCreate, db: Session = Depends(get_db)):
    # Verify referenced cliente exists
    get_or_404(db, Cliente, payload.id_cliente)
    obj = ContratoMudanca(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_contrato.patch("/{id_contrato}", response_model=ContratoMudancaResponse)
def update_contrato(id_contrato: int, payload: ContratoMudancaUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, ContratoMudanca, id_contrato)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_contrato.delete("/{id_contrato}", status_code=204)
def delete_contrato(id_contrato: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, ContratoMudanca, id_contrato)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# AlocacaoServico
# ─────────────────────────────────────────────

router_alocacao = APIRouter(prefix="/alocacoes", tags=["Alocacoes"])


@router_alocacao.get("/", response_model=List[AlocacaoServicoResponse])
def list_alocacoes(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(AlocacaoServico).offset(skip).limit(limit).all()


@router_alocacao.get("/{id_alocacao}", response_model=AlocacaoServicoResponse)
def get_alocacao(id_alocacao: int, db: Session = Depends(get_db)):
    return get_or_404(db, AlocacaoServico, id_alocacao)


@router_alocacao.post("/", response_model=AlocacaoServicoResponse, status_code=201)
def create_alocacao(payload: AlocacaoServicoCreate, db: Session = Depends(get_db)):
    get_or_404(db, ContratoMudanca, payload.id_contrato)
    obj = AlocacaoServico(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_alocacao.patch("/{id_alocacao}", response_model=AlocacaoServicoResponse)
def update_alocacao(id_alocacao: int, payload: AlocacaoServicoUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, AlocacaoServico, id_alocacao)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_alocacao.delete("/{id_alocacao}", status_code=204)
def delete_alocacao(id_alocacao: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, AlocacaoServico, id_alocacao)
    db.delete(obj)
    safe_commit(db)


# ─────────────────────────────────────────────
# ContratoPrestador
# ─────────────────────────────────────────────

router_contrato_prestador = APIRouter(prefix="/contrato-prestadores", tags=["ContratoPrestadores"])


@router_contrato_prestador.get("/", response_model=List[ContratoPrestadorResponse])
def list_contrato_prestadores(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return db.query(ContratoPrestador).offset(skip).limit(limit).all()


@router_contrato_prestador.get("/{id_cp}", response_model=ContratoPrestadorResponse)
def get_contrato_prestador(id_cp: int, db: Session = Depends(get_db)):
    return get_or_404(db, ContratoPrestador, id_cp)


@router_contrato_prestador.post("/", response_model=ContratoPrestadorResponse, status_code=201)
def create_contrato_prestador(payload: ContratoPrestadorCreate, db: Session = Depends(get_db)):
    get_or_404(db, ContratoMudanca, payload.id_contrato)
    get_or_404(db, Prestador, payload.id_prestador)
    obj = ContratoPrestador(**payload.model_dump())
    db.add(obj)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_contrato_prestador.patch("/{id_cp}", response_model=ContratoPrestadorResponse)
def update_contrato_prestador(id_cp: int, payload: ContratoPrestadorUpdate, db: Session = Depends(get_db)):
    obj = get_or_404(db, ContratoPrestador, id_cp)
    apply_patch(obj, payload)
    safe_commit(db)
    db.refresh(obj)
    return obj


@router_contrato_prestador.delete("/{id_cp}", status_code=204)
def delete_contrato_prestador(id_cp: int, db: Session = Depends(get_db)):
    obj = get_or_404(db, ContratoPrestador, id_cp)
    db.delete(obj)
    safe_commit(db)