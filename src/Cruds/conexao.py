import psycopg2 

import pandas   as pd 

import PySimpleGUI as sg

def conectando_servidor_postgres():
  

    try:
        
        df = pd.read_csv(r'servidorpadrao.csv',sep=',')
        valores = df['dados'].tolist()

        conn = psycopg2.connect(
            host    =valores[0],
            database=valores[1],
            user    =valores[2],
            password=valores[3]
        )
        cursor = conn.cursor()
        conn.close()
        sg.popup('conexao ok')

    except psycopg2.Error as e:
        sg.popup(str(e))


def dados():
    try:
        df = pd.read_csv(r'servidorpadrao.csv',sep=',')
        return df['dados'].tolist()
    except Exception as e:
        sg.popup(str(e))

#Crud Aluno
def inserir_alunos(values):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
INSERT INTO alunos(matricula,curso,nome,sobrenome,email,data_de_nascimento,número,rua,bairro,cidade,estado,sexo)
    values ({values[0]},{values[1]},'{values[2]}','{values[3]}','{values[4]}','{values[5]}',{values[6]},'{values[7]}','{values[8]}','{values[9]}','{values[10]}','{values[11]}');
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        Warning.inserido()
        
    except psycopg2.Error as e:
        Warning.get_message(str(e))




def crud_atualiza_alunos(values_new):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            UPDATE alunos
            SET 
                matricula = {values_new[0]},
                curso     = {values_new[1]},
                nome      = '{values_new[2]}',
                sobrenome = '{values_new[3]}',
                email     = '{values_new[4]}',
                data_de_nascimento = '{values_new[5]}',
                número    = {values_new[6]},
                rua       = '{values_new[7]}',
                bairro    = '{values_new[8]}' ,
                cidade    = '{values_new[9]}' ,
                estado    = '{values_new[10]}',
                sexo      = '{values_new[11]}'
            WHERE
                matricula = {values_new[0]};
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        Warning.atualizado()

    except psycopg2.Error as e:
        Warning.get_message(str(e))




def crud_remove_alunos(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            DELETE FROM alunos
            WHERE
                matricula = {id}
                '''
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
     

    except psycopg2.Error as e:
        Warning.get_message(str(e))




def condicao_existencia_alunos(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT a.matricula FROM alunos a
                where a.matricula = {id};
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



def select_alunos():

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM alunos a;
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




def select_alunos_especifico(id):

    try:
        valores = conexao.dados()

        conn = psycopg2.connect(
                host    =valores[0],
                database=valores[1],
                user    =valores[2],
                password=valores[3]
            )
            
                
        query = f'''
            SELECT * FROM alunos a
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

    except psycopg2.Error as e:
        Warning.get_message(str(e))

#Avaliações

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


#Blocos



