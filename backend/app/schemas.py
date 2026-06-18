"""
Estas schemas descrevem e validam a estruta dos dados que entram e saem da api. Destes dados, são gerados os docs openapi
"""

from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, Literal
from datetime import date
from decimal import Decimal


# ==================== Cliente Schemas ====================
class ClienteBase(BaseModel):
    nome: str = Field(..., min_length=1, max_length=30)
    data_nascimento: Optional[date] = None
    cpf: Optional[str] = Field(None, max_length=11)
    rg: Optional[str] = Field(None, max_length=9)
    email: Optional[str] = Field(None, max_length=30)
    contato: Optional[str] = Field(None, max_length=20)
    endereco: Optional[str] = Field(None, max_length=150)

    @field_validator("cpf")
    @classmethod
    def cpf_must_be_digits(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and (not v.isdigit() or len(v) != 11):
            raise ValueError("CPF must be exactly 11 numeric digits")
        return v


class ClienteCreate(ClienteBase):
    pass


class ClienteUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=30)
    data_nascimento: Optional[date] = None
    cpf: Optional[str] = Field(None, max_length=11)
    rg: Optional[str] = Field(None, max_length=9)
    email: Optional[str] = Field(None, max_length=30)
    contato: Optional[str] = Field(None, max_length=20)
    endereco: Optional[str] = Field(None, max_length=150)


class ClienteResponse(ClienteBase):
    model_config = ConfigDict(from_attributes=True)
    id_cliente: int


# ==================== Caminhao Schemas ====================
class CaminhaoBase(BaseModel):
    ultima_vistoria: Optional[date] = None
    crlv: Optional[str] = Field(None, max_length=12)


class CaminhaoCreate(CaminhaoBase):
    pass


class CaminhaoUpdate(BaseModel):
    ultima_vistoria: Optional[date] = None
    crlv: Optional[str] = Field(None, max_length=12)


class CaminhaoResponse(CaminhaoBase):
    model_config = ConfigDict(from_attributes=True)
    id_caminhao: int


# ==================== Prestador Schemas ====================
class PrestadorBase(BaseModel):
    nome: str = Field(..., min_length=1, max_length=30)
    data_nascimento: Optional[date] = None
    cpf: Optional[str] = Field(None, max_length=11)
    rg: Optional[str] = Field(None, max_length=9)
    cnh: Optional[str] = Field(None, max_length=9)
    email: Optional[str] = Field(None, max_length=30)
    contato: Optional[str] = Field(None, max_length=20)
    tipo_prestador: Literal["motorista", "ajudante", "outro"] = "ajudante"
    data_admissao: Optional[date] = None

    @field_validator("cpf")
    @classmethod
    def cpf_must_be_digits(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and (not v.isdigit() or len(v) != 11):
            raise ValueError("CPF must be exactly 11 numeric digits")
        return v


class PrestadorCreate(PrestadorBase):
    pass


class PrestadorUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=30)
    data_nascimento: Optional[date] = None
    cpf: Optional[str] = Field(None, max_length=11)
    rg: Optional[str] = Field(None, max_length=9)
    cnh: Optional[str] = Field(None, max_length=9)
    email: Optional[str] = Field(None, max_length=30)
    contato: Optional[str] = Field(None, max_length=20)
    tipo_prestador: Optional[Literal["motorista", "ajudante", "outro"]] = None
    data_admissao: Optional[date] = None


class PrestadorResponse(PrestadorBase):
    model_config = ConfigDict(from_attributes=True)
    id_prestador: int


# ==================== ServicoOferecido Schemas ====================
class ServicoOferecidoBase(BaseModel):
    nome: str = Field(..., min_length=1, max_length=60)
    descricao: Optional[str] = None
    quantidade_caixa_min: Optional[int] = Field(None, ge=0)
    quantidade_caixa_max: Optional[int] = Field(None, ge=0)
    requer_ajudante: bool = False
    preco: Optional[Decimal] = Field(None, gt=0, decimal_places=2)


class ServicoOferecidoCreate(ServicoOferecidoBase):
    pass


class ServicoOferecidoUpdate(BaseModel):
    nome: Optional[str] = Field(None, min_length=1, max_length=60)
    descricao: Optional[str] = None
    quantidade_caixa_min: Optional[int] = Field(None, ge=0)
    quantidade_caixa_max: Optional[int] = Field(None, ge=0)
    requer_ajudante: Optional[bool] = None
    preco: Optional[Decimal] = Field(None, gt=0, decimal_places=2)


class ServicoOferecidoResponse(ServicoOferecidoBase):
    model_config = ConfigDict(from_attributes=True)
    id_servico_oferecido: int


# ==================== ContratoMudanca Schemas ====================
class ContratoMudancaBase(BaseModel):
    id_cliente: int
    id_servico_oferecido: Optional[int] = None
    quantidade_caixa: Optional[int] = Field(None, ge=0)
    endereco_origem: Optional[str] = Field(None, max_length=150)
    endereco_destino: Optional[str] = Field(None, max_length=150)
    data_contrato: Optional[date] = None
    data_servico: Optional[date] = None
    forma_pagamento: Optional[Literal["pix", "credito", "debito", "dinheiro"]] = None


class ContratoMudancaCreate(ContratoMudancaBase):
    pass


class ContratoMudancaUpdate(BaseModel):
    id_servico_oferecido: Optional[int] = None
    quantidade_caixa: Optional[int] = Field(None, ge=0)
    endereco_origem: Optional[str] = Field(None, max_length=150)
    endereco_destino: Optional[str] = Field(None, max_length=150)
    data_contrato: Optional[date] = None
    data_servico: Optional[date] = None
    forma_pagamento: Optional[Literal["pix", "credito", "debito", "dinheiro"]] = None


class ContratoMudancaResponse(ContratoMudancaBase):
    model_config = ConfigDict(from_attributes=True)
    id_contrato: int


# ==================== AlocacaoServico Schemas ====================
class AlocacaoServicoBase(BaseModel):
    id_contrato: int
    id_caminhao: Optional[int] = None
    status_servico: Literal["pendente", "concluido"] = "pendente"
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class AlocacaoServicoCreate(AlocacaoServicoBase):
    pass


class AlocacaoServicoUpdate(BaseModel):
    id_caminhao: Optional[int] = None
    status_servico: Optional[Literal["pendente", "concluido"]] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None


class AlocacaoServicoResponse(AlocacaoServicoBase):
    model_config = ConfigDict(from_attributes=True)
    id_alocacao: int


# ==================== ContratoPrestador Schemas ====================
class ContratoPrestadorBase(BaseModel):
    id_contrato: int
    id_prestador: int
    funcao: Literal["motorista", "ajudante", "outro"] = "ajudante"


class ContratoPrestadorCreate(ContratoPrestadorBase):
    pass


class ContratoPrestadorUpdate(BaseModel):
    funcao: Optional[Literal["motorista", "ajudante", "outro"]] = None


class ContratoPrestadorResponse(ContratoPrestadorBase):
    model_config = ConfigDict(from_attributes=True)
    id_contrato_prestador: int