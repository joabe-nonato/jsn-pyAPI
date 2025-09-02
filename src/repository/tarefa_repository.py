from . import datasource
from model.tarefa import Tarefa

conn = datasource.conexao()

def listar():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Tarefa')
    result = []
    for row in cursor.fetchall():
        result.append(dict(zip([column[0] for column in cursor.description], row)))
    return result
    
def Obter(id : int):
    cursor = conn.cursor()    
    sql_query = 'SELECT TOP 1 * FROM Tarefa WHERE TarefaID = ?'
    cursor.execute(sql_query, id)
    row = cursor.fetchone()
    if row:
        columns = [column[0] for column in cursor.description]        
        return dict(zip(columns , row))
    return None

def Adicionar(tarefa: Tarefa):
    try:
        cursor = conn.cursor()
        sql_query = """
            INSERT INTO Tarefa (Fase, Titulo, Descricao, tema, Criado)
            OUTPUT INSERTED.TarefaID 
            VALUES (?, ?, ?, ?, GETDATE())
        """
        params = (            
            tarefa.Fase,
            tarefa.Titulo,
            tarefa.Descricao,
            tarefa.Tema
        )
        new_id = cursor.execute(sql_query, params).fetchval()
        conn.commit()
        print("Tarefa adicionada com sucesso")
        tarefa.TarefaID = new_id 
        return tarefa
    except Exception as e:
        conn.rollback()
        print(f"Ocorreu um erro ao adicionar a tarefa: {e}")
        return None

def Alterar(tarefa: Tarefa):
    try:
        cursor = conn.cursor()

        # Primeiro, verifica se a tarefa realmente existe
        cursor.execute('SELECT TarefaID FROM Tarefa WHERE TarefaID = ?', tarefa.TarefaID)
        if cursor.fetchone() is None:
            return None # Retorna None se não encontrar a tarefa

        sql_query = """
            UPDATE Tarefa
            SET Alterado = GETDATE(),
            Titulo = ?, Descricao = ?, Fase = ?, tema = ? WHERE TarefaID = ?
        """
        params = (
            tarefa.Titulo,
            tarefa.Descricao,
            tarefa.Fase,
            tarefa.Tema,
            tarefa.TarefaID
        )
        cursor.execute(sql_query, params)
        conn.commit()
        return tarefa # Retorna o objeto tarefa em caso de sucesso
    except Exception as e:
        conn.rollback()
        print(f"Ocorreu um erro ao alterar a tarefa: {e}")
        return None # Retorna None em caso de erro

def Excluir(tarefa_id: int):
    try:
        cursor = conn.cursor()
        sql_query = "DELETE FROM Tarefa WHERE TarefaID = ?"
        cursor.execute(sql_query, tarefa_id)
        conn.commit()
        return cursor.rowcount
    except Exception as e:
        conn.rollback()
        print(f"Ocorreu um erro ao excluir a tarefa: {e}") # Mensagem corrigida
        return 0