import pandas as pd
import psycopg2
import PySimpleGUI as sg

from  src.Interface import Warning
from  src.Cruds import conexao


def inserir_local(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO locais(ID_local,tipo,bloco,lotacao,nome,descricao)
                values ({values[0]},'{values[1]}',{values[2]},{values[3]},'{values[4]}','{values[5]}');
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.inserido()
        
    except psycopg2.Error as e:
        Warning.get_message(str(e))




def crud_atualiza_local(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE locais p
            SET 
                tipo      = '{values_new[1]}',
                bloco     =  {values_new[2]},
                lotacao   =  {values_new[3]},
                nome      = '{values_new[4]}',
                descricao = '{values_new[5]}'
            WHERE
                id_local = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()
    except psycopg2.Error as e:
        Warning.get_message(str(e))



def crud_remove_local(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM locais
            WHERE
                id_local = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
     

    except psycopg2.Error as e:
        Warning.get_message(str(e))




def condicao_existencia_local(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT p.ID_local FROM locais p
                where p.ID_local = {id};
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

    except psycopg2.Error as e:
        Warning.get_message(str(e))



def select_local():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM locais p;
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




def select_local_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM locais p
                where p.ID_local = {id};
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

    except psycopg2.Error as e:
        Warning.get_message(str(e))


