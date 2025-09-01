from fastapi import APIRouter, HTTPException, status
from model.tarefa import Tarefa
from service.tarefa_service import *


router = APIRouter()

@router.get("/listar/", response_model=list[Tarefa])
def atividades():
    return Listar()

@router.get("/obter/{atividadeID}", response_model=Tarefa)
def atividade_obter(atividadeID: int):
    tarefa = Obter(atividadeID)
    if tarefa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarefa com ID {atividadeID} não encontrada.")
    return tarefa

@router.post("/adicionar/", response_model=Tarefa, status_code=status.HTTP_201_CREATED)
def atividade_adicionar(tarefa: Tarefa):
    nova_tarefa = Adicionar(tarefa)
    if nova_tarefa is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Ocorreu um erro ao adicionar a tarefa.")
    return nova_tarefa

@router.put("/alterar/{atividadeID}", response_model=Tarefa)
def atividade_alterar(atividadeID: int, tarefa: Tarefa):
    if atividadeID != tarefa.TarefaID:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="O ID da URL não corresponde ao ID do corpo da requisição.")
    
    tarefa_alterada = Alterar(tarefa)
    if tarefa_alterada is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não foi possível alterar a tarefa com ID {atividadeID}, pois ela não foi encontrada.")
    
    return tarefa_alterada

@router.delete("/excluir/{atividadeID}", status_code=status.HTTP_204_NO_CONTENT)
def atividade_excluir(atividadeID: int):
    linhas_afetadas = Excluir(atividadeID)
    if linhas_afetadas == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Tarefa com ID {atividadeID} não encontrada para exclusão.")
    
    return None
