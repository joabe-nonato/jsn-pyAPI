from pydantic import BaseModel

class Tarefa(BaseModel):
    TarefaID: int   
    Fase: str | None = None
    Titulo: str | None = None
    Descricao: str | None = None
    Tema: str | None = None    


