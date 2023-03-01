import pandas as pd
import psycopg2
import PySimpleGUI as sg

from  src.Interface import Warning
from  src.Cruds import conexao


def inserir_turmas(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            INSERT INTO turmas(id_turma,ano,semestre,disciplina,estado,loca_l,horario_inicio,horario_fim,vagas,qtde_matriculados)
                values ({values[0]},{values[1]},{values[2]},{values[3]},'{values[4]}',{values[5]},'{values[6]}','{values[7]}',{values[8]},{values[9]});
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.inserido()
        
    except psycopg2.Error as e:
        print(str(e))
        Warning.get_message(str(e))




def crud_atualiza_turmas(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE turmas 
            SET 
                ano        = {valores[0]},
                semestre   = {valores[1]},
                disciplina = {valores[2]},
                estado     = '{valores[3]}',
                loca_l     = {valores[4]}, 
                horario_inicio = {valores[5]},
                horario_fim    = {valores[6]},
                vagas            = {valores[7]},
                qtde_matriculados = {valores[8]}
            WHERE
                id_turma = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()
    except psycopg2.Error as e:
        Warning.get_message(str(e))



def crud_remove_turmas(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM turmas
            WHERE
                id_turmas = {id}
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
     

    except psycopg2.Error as e:
        Warning.get_message(str(e))




def condicao_existencia_turmas(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT p.id_turma FROM turmas p
                where p.id_turma = {id};
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



def select_turmas():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM turmas p;
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




def select_turmas_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM turmas p
                where p.id_turma = {id};
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


