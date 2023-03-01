import pandas as pd
import PySimpleGUI as sg

from   src.Interface import menu
from   src.consultas_especiais import consultas_interface

from   src.Cruds import conexao
from   src.Operecao_com_interface import professores
from   src.Operecao_com_interface import reitor
from   src.Operecao_com_interface import campus
from   src.Operecao_com_interface import centros
from   src.Operecao_com_interface import cursos
from   src.Operecao_com_interface import aluno
from   src.Operecao_com_interface import prof_curso
from   src.Operecao_com_interface import consulta_especias
from   src.Operecao_com_interface import disciplinas
from   src.Operecao_com_interface import bloco
from   src.Operecao_com_interface import local
from   src.Operecao_com_interface import turmas
from   src.Operecao_com_interface import dia_semana
from   src.Operecao_com_interface import matriculas
from   src.Operecao_com_interface import avaliacoes

def main():
    
    sg.theme('DarkBlue')
    while True:
        janela_menu = menu.menu()
        event , values = janela_menu.read()

        if (event=='Sair' or event==sg.WIN_CLOSED):break
        
        match (event):
            case 'Conectar ao Servidor': 
                janela_menu.hide()      
                conexao()


            case 'Professor':
                janela_menu.hide()
                professores.menu_professor(event)

            case 'Reitor':
                janela_menu.hide()
                reitor.menu_reitor(event)

            case 'Campus':
                janela_menu.hide()
                campus.menu_campus(event)

            case 'Centros':
                janela_menu.hide()
                centros.menu_centros(event)
                
            case 'Curso':
                janela_menu.hide()
                cursos.menu_cursos(event)

            case 'Aluno':
                janela_menu.hide()
                aluno.menu_aluno(event)
            
            case 'Disciplina':
                janela_menu.hide()
                disciplinas.menu_disciplina(event)
            
            case 'Prof Curso':
                janela_menu.hide()
                prof_curso.menu_prof_curso(event)

            case 'Avaliações':
                janela_menu.hide()
                avaliacoes.menu_avaliacoes(event)
                
            
            case 'Blocos':
                janela_menu.hide()
                bloco.menu_bloco(event)
            
            case 'Locais':
                janela_menu.hide()
                local.menu_local(event)
    
            case 'Turmas':
                janela_menu.hide()
                turmas.menu_turmas(event)
            
            case 'Dia_Semana':
                janela_menu.hide()
                dia_semana.menu_dia_semana(event)

            case 'Matriculas':
                janela_menu.hide()
                matriculas.menu_matricula(event)
            

            case 'Consulta1':
                janela_menu.hide()
                consulta_especias.consulta_1()
            
            case 'Consulta2':
                janela_menu.hide()
                consultas_interface.consulta2()
            
            case 'Consulta3':
                janela_menu.hide()
                consultas_interface.consulta3()

            case 'Consulta4':
                janela_menu.hide()
                consultas_interface.consulta4()

            case 'Consulta5':
                janela_menu.hide()
                consultas_interface.consulta5()

                


                

            
def conexao():
    janela_conexao = menu.servidor()

    while True:
        
        event,values   = janela_conexao.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Continuar'):
            host     = values['host']
            database = values['database']
            user     = values['user']
            password = values['password']
            
            pd.DataFrame({'dados':[host,database,user,password]}).to_csv('servidorpadrao.csv',index=False)
        
    janela_conexao.close()


if __name__=='__main__':
    main()