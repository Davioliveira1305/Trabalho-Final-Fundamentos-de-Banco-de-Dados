import pandas as pd
import psycopg2

from src.Interface import Warning
from src.Cruds import conexao


def select_cursos():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM cursos c;
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

    except psycopg2.Error:
        print('Erro na operacao de existencia')




def select_cursos_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM cursos c
                where c.id_curso = {id};
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

    except psycopg2.Error:
        print('Erro na operacao de existencia')




def inserir_cursos(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO cursos(id_curso,nome,centro,coordenador,carga_horaria)
                values ({values[0]},'{values[1]}',{values[2]},{values[3]},{values[4]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.inserido()  

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))




def crud_atualiza_cursos(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE cursos
            SET 
                id_curso      = {values_new[0]},
                nome          = '{values_new[1]}',
                centro        = {values_new[2]},
                coordenador   = {values_new[3]},
                carga_horaria = {values_new[4]}
            WHERE
                id_curso = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()
     

    except (psycopg2.Error ,Exception) as e:
        Warning.get_message(str(e))
        




def crud_remove_cursos(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM cursos
            WHERE
                id_curso = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.removido()
        
    except psycopg2.Error as e:
        Warning.get_message(str(e))




def condicao_existencia_cursos(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT c.id_curso FROM cursos c
                where c.id_curso = {id};
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

    except psycopg2.Error as e :
        Warning.get_message(str(e))


