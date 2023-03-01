import pandas as pd
import psycopg2
import PySimpleGUI as sg

from   src.Cruds import conexao
from   src.Interface import Warning


def select_matricula():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM matriculas ;
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




def select_matricula_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM matriculas 
                where matricula = {id};
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




def inserir_matricula(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO matriculas(matricula,turma)
                values ({values[0]},'{values[1]}');
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.inserido()  

    except (psycopg2.Error, Exception) as e:
        Warning.get_message(str(e))





def crud_remove_matricula(matricula):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM matriculas
            WHERE
                matricula = {matricula};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.get_message('Removido')
    except (psycopg2.DatabaseError, psycopg2.Error, Exception) as e:  
        Warning.get_message(str(e)) 
    
