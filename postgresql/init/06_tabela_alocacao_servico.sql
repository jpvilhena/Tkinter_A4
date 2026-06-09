-- This file now defines the service allocation and the many-to-many contract/prestador assignment.

CREATE TABLE IF NOT EXISTS alocacao_servico (
    id_alocacao INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_contrato INT NOT NULL,
    id_caminhao INT,
    status_servico VARCHAR(10) NOT NULL DEFAULT 'pendente',
    data_inicio DATE,
    data_fim DATE,

    CHECK (status_servico IN ('pendente', 'concluido')),

    FOREIGN KEY (id_contrato)
        REFERENCES contrato_mudanca(id_contrato)
        ON DELETE CASCADE,

    FOREIGN KEY (id_caminhao)
        REFERENCES caminhao(id_caminhao)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS contrato_prestador (
    id_contrato_prestador INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_contrato INT NOT NULL,
    id_prestador INT NOT NULL,
    funcao VARCHAR(20) NOT NULL DEFAULT 'ajudante',

    CHECK (funcao IN ('motorista', 'ajudante', 'outro')),
    UNIQUE (id_contrato, id_prestador),

    FOREIGN KEY (id_contrato)
        REFERENCES contrato_mudanca(id_contrato)
        ON DELETE CASCADE,

    FOREIGN KEY (id_prestador)
        REFERENCES prestador(id_prestador)
        ON DELETE CASCADE
);
