import pandas as pd

from server_engine import Database


db = Database()

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
}


def run_query(sql: str) -> pd.DataFrame:
    rows = db.query(sql)
    return pd.DataFrame(rows)


def close_database() -> None:
    db.close()

