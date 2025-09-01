from pydantic import BaseModel

class Tarefa(BaseModel):
    TarefaID: int   
    Id: str | None = None
    Fase: str | None = None
    Titulo: str | None = None
    Descricao: str | None = None
    Tema: str | None = None    


