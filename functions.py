"""Encapsulates saved SQL queries and database helper functions."""

import pandas as pd

from server_engine import Database


# Create a shared Database instance used by the application helpers.
db = Database()

# This dict has the title that will display on the aplication as a key and the sql query that will run as its value
# We can add as many values as we want here to add more options for showing data
QUERY_OPTIONS = {
    "Ajudantes por total de serviços": """
        SELECT
            a.id_ajudante,
            a.nome,
            COUNT(h.id_equipe) AS total_servicos
        FROM ajudante a
        LEFT JOIN historico_equipe_servico h
            ON h.id_ajudante = a.id_ajudante
        GROUP BY a.id_ajudante, a.nome
        ORDER BY total_servicos DESC;
    """,
    "Serviços cada caminhão participou":"""
        SELECT
            c.id_caminhao,
            COUNT(h.id_equipe) AS total_usos
        FROM caminhao c
        LEFT JOIN historico_equipe_servico h
            ON h.id_caminhao = c.id_caminhao
        GROUP BY c.id_caminhao
        ORDER BY total_usos DESC;
    """,
    "Total de serviços cadastrados por cliente": """
        SELECT 
            c.id_cliente,
            c.nome,
            COUNT(s.id_servico) AS total_servicos
        FROM cliente c
        LEFT JOIN servico_mudanca s ON s.id_cliente = c.id_cliente
        GROUP BY c.id_cliente, c.nome
        ORDER BY total_servicos DESC;
    """,
    "Agrupar os serviços concluídos x pendentes": """
    SELECT 
            status_servico,
            COUNT(id_equipe) AS total
        FROM historico_equipe_servico
        GROUP BY status_servico;
    """,
    "Quantos serviços cada motorista participou":"""
        SELECT 
            m.id_motorista,
            m.nome,
            COUNT(h.id_equipe) AS total_servicos
        FROM motorista m
        LEFT JOIN historico_equipe_servico h 
            ON h.id_motorista = m.id_motorista
        GROUP BY m.id_motorista, m.nome
        ORDER BY total_servicos DESC;
    """,
    "Apuração da  forma de pagamento mais usada pelos clientes":"""
    SELECT forma_pagamento, COUNT(*) AS quantidade_vezes_usado
    FROM servico_mudanca
    GROUP BY forma_pagamento
    ORDER BY quantidade_vezes_usado DESC
    LIMIT 1;
"""
}


def run_query(sql: str) -> pd.DataFrame:
    """Execute a saved SQL query and return the results as a pandas DataFrame."""
    rows = db.query(sql)
    return pd.DataFrame(rows)


def close_database() -> None:
    """Close the shared database connection when the app exits."""
    db.close()

