# Todo App API

> Uma API simples de gerenciamento de tarefas (TODO) construída com FastAPI, SQLAlchemy e SQLite.

## Requisitos

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/todo_app.git
   cd todo_app

Acesse a documentação interativa em: http://localhost:8000/docs

Endpoints principais
POST   /api/todos/ - Criar uma nova tarefa
GET    /api/todos/ - Listar todas as tarefas
GET    /api/todos/{id} - Buscar tarefa por ID
PUT    /api/todos/{id} - Atualizar tarefa
DELETE /api/todos/{id} - Remover tarefa
Estrutura do projeto
main.py - Inicialização do app FastAPI
routes.py - Rotas e lógica dos endpoints
models.py - Modelos ORM SQLAlchemy
schemas.py - Schemas Pydantic
database.py - Configuração do banco de dados
Observações
O banco padrão é SQLite, mas pode ser adaptado facilmente para outros bancos.
Acesse /docs para testar a API via Swagger UI.
Feito com FastAPI 🚀


