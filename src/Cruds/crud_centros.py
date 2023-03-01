import pandas as pd
import psycopg2

from src.Interface import Warning
from src.Cruds import conexao


def select_centros():


    try:
        valores = conexao.dados()
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM centros c;
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



def select_centros_especifico(id):
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM centros c
                where c.id_centro = {id};
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




def inserir_centros(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO centros(id_centro,nome,diretor,campus)
                values ({values[0]},'{values[1]}',{values[2]},{values[3]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        return True    
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def crud_atualiza_centros(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE centros
            SET 
                id_centro    = {values_new[0]},
                nome         = '{values_new[1]}',
                diretor      = '{values_new[2]}',
                campus       = '{values_new[3]}'
            WHERE
                id_centro = {values_new[0]};
                '''

        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        Warning.atualizado()
     

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))



def crud_remove_centros(id):
 
    try:
        valores = conexao.dados()
 
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM centros
            WHERE
                id_centro = {id};
                '''
        
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        Warning.removido()
        
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))

def condicao_existencia_centros(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT c.id_centro FROM centros c
                where c.id_centro = {id};
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


