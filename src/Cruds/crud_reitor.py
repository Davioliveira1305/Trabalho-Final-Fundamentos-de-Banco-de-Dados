import pandas as pd
import psycopg2
import PySimpleGUI as sg

from src.Cruds import conexao
from   src.Interface import Warning


def select_reitor():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM reitores r;
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




def select_reitor_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM reitores r
                where p.id_reitor = {id};
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




def inserir_reitor(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO reitores(id_reitor,data_de_admissao)
                values ({values[0]},'{values[1]}');
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.inserido()  

    except (psycopg2.Error, Exception) as e:
        Warning.get_message(str(e))




def crud_atualiza_reitor(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE reitores
            SET 
                id_reitor    = {values_new[0]}

            WHERE
                id_professor = {values_new[3]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()

    except (psycopg2.Error,Exception) as e:
        Warning.get_message(str(e))
        


def crud_remove_reitor(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM reitores
            WHERE
                id_reitor = {id};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.get_message('Removido')
    except (psycopg2.DatabaseError, psycopg2.Error, Exception) as e:  
        Warning.get_message(str(e)) 
    
