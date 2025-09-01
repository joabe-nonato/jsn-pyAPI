from model.tarefa import Tarefa
import repository.tarefa_repository as r

def Listar():    
    return r.listar()
    
def Obter(id : int):
    return r.Obter(id)

def Adicionar(tarefa: Tarefa):
    return r.Adicionar(tarefa)

def Alterar(tarefa: Tarefa):
    return r.Alterar(tarefa)

def Excluir(id: int):
    return r.Excluir(id)
