from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

# Permitir chamadas do seu site local
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # libera apenas essas origens
    allow_credentials=True,
    allow_methods=["*"],         # libera todos os métodos (GET, POST, etc)
    allow_headers=["*"],         # libera todos os headers
)

# Rotas
app.include_router(
    atividades.router,
    prefix="/atividade",
    tags=["Atividades"],
)
