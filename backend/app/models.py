"""
Estes modelos descrevem e validam a estrutura dos dados guardados no banco de dados
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Text,
    ForeignKey,
    CheckConstraint,
    UniqueConstraint,
    Numeric,
    Boolean,
)

from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Cliente(Base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    data_nascimento = Column(Date)
    cpf = Column(String(11), unique=True)
    rg = Column(String(9))
    email = Column(String(30))
    contato = Column(String(20))
    endereco = Column(String(150))

    contratos = relationship("ContratoMudanca", back_populates="cliente")

    def __repr__(self):
        return f"<Cliente id={self.id_cliente} nome={self.nome!r}>"


class Caminhao(Base):
    __tablename__ = "caminhao"

    id_caminhao = Column(Integer, primary_key=True, autoincrement=True)
    ultima_vistoria = Column(Date)
    crlv = Column(String(12), unique=True)

    alocacoes = relationship("AlocacaoServico", back_populates="caminhao")

    def __repr__(self):
        return f"<Caminhao id={self.id_caminhao} crlv={self.crlv!r}>"


class Prestador(Base):
    __tablename__ = "prestador"

    id_prestador = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30), nullable=False)
    data_nascimento = Column(Date)
    cpf = Column(String(11), unique=True)
    rg = Column(String(9))
    cnh = Column(String(9))
    email = Column(String(30))
    contato = Column(String(20))
    tipo_prestador = Column(String(20), default="ajudante", nullable=False)
    data_admissao = Column(Date)

    contratos = relationship("ContratoPrestador", back_populates="prestador")

    __table_args__ = (
        CheckConstraint("tipo_prestador IN ('motorista', 'ajudante', 'outro')"),
    )

    def __repr__(self):
        return f"<Prestador id={self.id_prestador} nome={self.nome!r} tipo={self.tipo_prestador!r}>"


class ServicoOferecido(Base):
    __tablename__ = "servico_oferecido"

    id_servico_oferecido = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(60), nullable=False)
    descricao = Column(Text)
    quantidade_caixa_min = Column(Integer)
    quantidade_caixa_max = Column(Integer)
    requer_ajudante = Column(Boolean, default=False)
    preco = Column(Numeric(12, 2))

    contratos = relationship("ContratoMudanca", back_populates="servico")

    __table_args__ = (
        CheckConstraint("quantidade_caixa_min >= 0"),
        CheckConstraint("quantidade_caixa_max >= quantidade_caixa_min"),
    )

    def __repr__(self):
        return f"<ServicoOferecido id={self.id_servico_oferecido} nome={self.nome!r}>"


class ContratoMudanca(Base):
    __tablename__ = "contrato_mudanca"

    id_contrato = Column(Integer, primary_key=True, autoincrement=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id_cliente"), nullable=False)
    id_servico_oferecido = Column(Integer, ForeignKey("servico_oferecido.id_servico_oferecido"))
    quantidade_caixa = Column(Integer)
    endereco_origem = Column(String(150))
    endereco_destino = Column(String(150))
    data_contrato = Column(Date)
    data_servico = Column(Date)
    forma_pagamento = Column(String(10))

    cliente = relationship("Cliente", back_populates="contratos")
    servico = relationship("ServicoOferecido", back_populates="contratos")
    alocacoes = relationship("AlocacaoServico", back_populates="contrato")
    prestadores = relationship("ContratoPrestador", back_populates="contrato")

    __table_args__ = (
        CheckConstraint("forma_pagamento IN ('pix','credito','debito','dinheiro')"),
    )

    def __repr__(self):
        return f"<ContratoMudanca id={self.id_contrato} cliente={self.id_cliente}>"


class AlocacaoServico(Base):
    __tablename__ = "alocacao_servico"

    id_alocacao = Column(Integer, primary_key=True, autoincrement=True)
    id_contrato = Column(Integer, ForeignKey("contrato_mudanca.id_contrato"), nullable=False)
    id_caminhao = Column(Integer, ForeignKey("caminhao.id_caminhao"))
    status_servico = Column(String(10), default="pendente", nullable=False)
    data_inicio = Column(Date)
    data_fim = Column(Date)

    contrato = relationship("ContratoMudanca", back_populates="alocacoes")
    caminhao = relationship("Caminhao", back_populates="alocacoes")

    __table_args__ = (
        CheckConstraint("status_servico IN ('pendente', 'concluido')"),
    )

    def __repr__(self):
        return f"<AlocacaoServico id={self.id_alocacao} status={self.status_servico!r}>"


class ContratoPrestador(Base):
    __tablename__ = "contrato_prestador"

    id_contrato_prestador = Column(Integer, primary_key=True, autoincrement=True)
    id_contrato = Column(Integer, ForeignKey("contrato_mudanca.id_contrato"), nullable=False)
    id_prestador = Column(Integer, ForeignKey("prestador.id_prestador"), nullable=False)
    funcao = Column(String(20), default="ajudante", nullable=False)

    contrato = relationship("ContratoMudanca", back_populates="prestadores")
    prestador = relationship("Prestador", back_populates="contratos")

    __table_args__ = (
        CheckConstraint("funcao IN ('motorista', 'ajudante', 'outro')"),
        UniqueConstraint("id_contrato", "id_prestador", name="uq_contrato_prestador"),
    )

    def __repr__(self):
        return f"<ContratoPrestador contrato={self.id_contrato} prestador={self.id_prestador}>"