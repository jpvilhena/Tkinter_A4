# MudaExpress Backend

API FastAPI para gerenciamento de clientes, caminhões, motoristas, ajudantes e serviços.

Setup rápido

1. Crie um ambiente virtual e instale dependências:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Configure a variável de ambiente `DATABASE_URL` para apontar ao seu PostgreSQL. Exemplo:

```powershell
$env:DATABASE_URL = "postgresql://postgres:password@localhost:5432/mudaexpress"
```

3. Execute a aplicação:

```powershell
python main.py
# ou
uvicorn app.main:app --reload
```

Rotas principais

- `/clients` - CRUD clientes
- `/trucks` - CRUD caminhões
- `/drivers` - CRUD motoristas
- `/helpers` - CRUD ajudantes
- `/services` - CRUD serviços (associa caminhões, motoristas e ajudantes)

Notas

- A criação de serviços exige que o cliente exista previamente.
- Ajuste `DATABASE_URL` conforme seu ambiente PostgreSQL.
