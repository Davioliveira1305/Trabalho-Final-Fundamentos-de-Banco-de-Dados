import pandas as pd
import psycopg2

from  src.Cruds import conexao
from  src.Interface import Warning


def select_campus():
   
    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM campus c;
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





def select_campus_especifico(id):


    try:
        valores = conexao.dados()
        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM campus c
                where c.id_campus = {id};
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





def inserir_campus(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO campus(id_campus,nome,reitor,local_campus)
                values ({values[0]},'{values[1]}','{values[2]}','{values[3]}');
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        
        return True    

    except psycopg2.Error:
        Warning.erro_i()
        return False 




def crud_atualiza_campus(values_new):

 
 

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE campus
            SET 
                id_campus    = {values_new[0]}  ,
                nome         = '{values_new[1]}',
                reitor       =  {values_new[2]} ,
                local_campus = '{values_new[3]}'
            WHERE
                id_campus = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.atualizado()
     
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))





def crud_remove_campus(id):


    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM campus
            WHERE
                id_campus = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)

        conn.commit()
        conn.close()
        return True
        
    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))




def condicao_existencia_campus(id):


    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT c.id_campus FROM campus c
                where c.id_campus = {id};
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




