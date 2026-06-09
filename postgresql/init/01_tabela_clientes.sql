CREATE TABLE IF NOT EXISTS cliente (
    id_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome VARCHAR(30) NOT NULL,
    data_nascimento DATE,
    cpf VARCHAR(11) UNIQUE,
    rg VARCHAR(9),
    email VARCHAR(30),
    contato VARCHAR(20),
    endereco VARCHAR(150)
);