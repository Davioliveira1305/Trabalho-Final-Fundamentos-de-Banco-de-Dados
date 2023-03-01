import pandas as pd
import psycopg2
import PySimpleGUI as sg

from  src.Interface import Warning
from  src.Cruds import conexao


def inserir_disciplina(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO disciplinas(id_disciplina,nome,professor,ementa,carga_horaria)
                values ({values[0]},'{values[1]}',{values[2]},'{values[3]}',{values[4]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.inserido()
        
    except psycopg2.Error as e:
        Warning.get_message(str(e))




def crud_atualiza_disciplina(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE disciplinas 
            SET 
                nome          = '{values_new[1]}',
                professor     =  {values_new[2]},
                ementa        = '{values_new[3]}',
                carga_horaria =  {values_new[4]}
            WHERE
                id_disciplina = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()
    except psycopg2.Error as e:
        Warning.get_message(str(e))



def crud_remove_disciplina(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM disciplinas
            WHERE
                id_disciplina = {id}
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
     

    except psycopg2.Error as e:
        Warning.get_message(str(e))




def condicao_existencia_disciplina(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT p.id_disciplina FROM disciplinas p
                where p.id_disciplina = {id};
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



def select_disciplina():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM disciplinas p;
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




def select_disciplina_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM disciplinas p
                where p.id_disciplina = {id};
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


