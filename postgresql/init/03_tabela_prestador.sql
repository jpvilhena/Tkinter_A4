-- This table replaces the previous ajudante/motorista split.
-- Use a single prestador table for all service providers.

CREATE TABLE IF NOT EXISTS prestador (
    id_prestador INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    data_nascimento DATE,
    cpf VARCHAR(11) UNIQUE,
    rg VARCHAR(9),
    cnh VARCHAR(9),
    email VARCHAR(30),
    contato VARCHAR(20),
    tipo_prestador VARCHAR(20) NOT NULL DEFAULT 'ajudante',
    data_admissao DATE,
    CHECK (tipo_prestador IN ('motorista', 'ajudante', 'outro'))
);
