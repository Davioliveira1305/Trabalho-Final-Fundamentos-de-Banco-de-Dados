import pandas as pd
import psycopg2

from  src.Cruds import conexao
from  src.Interface import Warning


def inserir_prof_curso(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO prof_cursos(id_professor,id_curso)
                values ({values[0]},{values[1]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        
        Warning.inserido()  

    except psycopg2.Error:
        Warning.erro_i()
        return False 




def crud_atualiza_prof_curso(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE prof_cursos
            SET 
                id_professor  = {values_new[0]},
                id_curso      = {values_new[1]}
            WHERE
                id_professor = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.atualizado()
     
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def crud_remove_prof_curso(id):


    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM prof_cursos
            WHERE
                id_professor = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        return True
        
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))




def condicao_existencia_prof_curso(id):


    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT c.id_professor FROM prof_cursos c
                where c.id_professor = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        valor = cursor.fetchall()
        conn.close()
        try:
            teste = valor[0][0]
            return True

        except Exception:
            return False

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def select_prof_curso():
   
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM prof_cursos c;
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

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def select_prof_curso_especifico(id):


    try:
        valores = conexao.dados()
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM prof_cursos c
                where c.id_professor = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        valor = cursor.fetchall()
        
        conn.close()

        try:       
            teste = valor[0][0]
            return valor[0]

        except Exception:
            return False

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))


