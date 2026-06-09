-- This table represents the customer contract / order, separated from the service catalogue.

CREATE TABLE IF NOT EXISTS contrato_mudanca (
    id_contrato INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_servico_oferecido INT,
    quantidade_caixa INT,
    endereco_origem VARCHAR(150),
    endereco_destino VARCHAR(150),
    data_contrato DATE,
    data_servico DATE,
    forma_pagamento VARCHAR(10),

    CHECK (forma_pagamento IN ('pix','credito','debito','dinheiro')),

    FOREIGN KEY (id_cliente)
        REFERENCES cliente(id_cliente)
        ON DELETE RESTRICT,

    FOREIGN KEY (id_servico_oferecido)
        REFERENCES servico_oferecido(id_servico_oferecido)
        ON DELETE SET NULL
);
