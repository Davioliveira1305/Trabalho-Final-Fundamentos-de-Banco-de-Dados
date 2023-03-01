import psycopg2
from   src.Cruds import conexao
from   src.Interface import Warning
def visualizar_media():
    
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            select A.matricula,A.ID_Disciplina, AVG(A.Nota) from avaliacoes A, Turmas T, Matriculas M
                where M.Matricula = A.Matricula and M.Turma = T.ID_Turma  and T.Estado = 'CONCLUÍDA'
            group by A.matricula,A.ID_Disciplina;
                '''

        cursor = conn.cursor()
        cursor.execute(query)
        
        valor = cursor.fetchall()
        
        conn.close()

        try:   
            teste = valor[0][0]
            return valor

        except Exception:
            return False

    except psycopg2.Error as e:
        Warning.get_message(str(e))
    


def localizacao(valor):
    
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            select ID_Local, Nome from Locais where bloco = {valor};
                '''

        cursor = conn.cursor()
        cursor.execute(query)
        
        valor = cursor.fetchall()
        
        conn.close()

        try:   
            teste = valor[0][0]
            return valor

        except Exception:
            return False

    except psycopg2.Error as e:
        Warning.get_message(str(e))



def turmas(valor):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            Select T.ID_Turma, D.Nome, T.Horario_inicio, T.Horario_Fim from Turmas T, Disciplinas D
                where D.ID_Disciplina = T.Disciplina  and T.Loca_l = {valor};
                '''

        cursor = conn.cursor()
        cursor.execute(query)
        
        valor = cursor.fetchall()
        
        conn.close()

        try:   
            teste = valor[0][0]
            return valor

        except Exception:
            return False

    except psycopg2.Error as e:
        Warning.get_message(str(e))


def medias_aluno(valor):
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
        select A.matricula,A.ID_Disciplina, AVG(A.Nota) from avaliacoes A, Turmas T, Matriculas M
            where M.Matricula = A.Matricula and M.Turma = T.ID_Turma and A.Matricula = {valor}
            group by A.matricula,A.ID_Disciplina;
                '''

        cursor = conn.cursor()
        cursor.execute(query)
        
        valor = cursor.fetchall()
        
        conn.close()

        try:   
            teste = valor[0][0]
            return valor

        except Exception:
            return False

    except psycopg2.Error as e:
        Warning.get_message(str(e))


def historico(valor):
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
        select ID_Turma, Ano, semestre from turmas where ano = {valor[0]} and semestre = {valor[1]};
                '''

        cursor = conn.cursor()
        cursor.execute(query)
        
        valor = cursor.fetchall()
        
        conn.close()

        try:   
            teste = valor[0][0]
            return valor

        except Exception:
            return False

    except psycopg2.Error as e:
        Warning.get_message(str(e))

