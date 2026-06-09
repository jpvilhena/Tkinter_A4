-- This table now defines offered moving services and their parameters.
-- Contracts should reference these service definitions separately.

CREATE TABLE IF NOT EXISTS servico_oferecido (
    id_servico_oferecido INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(60) NOT NULL,
    descricao TEXT,
    quantidade_caixa_min INT,
    quantidade_caixa_max INT,
    requer_ajudante BOOLEAN DEFAULT FALSE,
    preco NUMERIC(12,2),
    CHECK (quantidade_caixa_min >= 0),
    CHECK (quantidade_caixa_max >= quantidade_caixa_min)
);
