
import pandas as pd
import psycopg2

from src.Interface import Warning
from src.Cruds import conexao


def select_avaliacoes():


    try:
        valores = conexao.dados()
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM avaliacoes a;
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



def select_avaliacoes_especifico(id):
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM avaliacoes a
                where a.matricula = {id};
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




def inserir_avaliacoes(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO avaliacoes(matricula,tipo,id_disciplina,nota)
                values ({values[0]},'{values[1]}',{values[2]},{values[3]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.inserido()  
          
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def crud_atualiza_avaliacoes(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE avaliacoes
            SET 
                matricula      = {values_new[0]},
                tipo           = '{values_new[1]}',
                id_disciplina  = {values_new[2]},
                nota           = {values_new[3]}
            WHERE
                matricula      = {values_new[0]};
                '''

        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        Warning.atualizado()
     

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))



def crud_remove_avaliacoes(id):
 
    try:
        valores = conexao.dados()
 
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM avaliacoes
            WHERE
                matricula = {id};
                '''
        
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        Warning.removido()
        
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))

def condicao_existencia_avaliacoes(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT a.matricula FROM avaliacoes a
                where matricula = {id};
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


