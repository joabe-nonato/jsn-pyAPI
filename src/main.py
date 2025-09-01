from fastapi import FastAPI
from routers import atividades

app = FastAPI(
    title="API de Gestão de Tarefas",
    version="1.0.0",
    description="API completa para criar, alterar, listar e excluir tarefas.",
    contact={
        "name": "Joabe Nonato",
        "url": "https://github.com/joabe-nonato",
        "email": "joabe07@gmail.com",
    },
)

app.include_router(
    atividades.router,
    prefix="/atividade",
    tags=["Atividades"],
)