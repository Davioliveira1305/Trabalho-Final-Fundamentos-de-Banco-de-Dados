from src.Interface import menu
from src.Interface import i_matricula

from src.Cruds import crud_matricula
from src.Cruds import crud_professor

import PySimpleGUI as sg 

def menu_matricula(dtype):
    

    while True:
        janela_menu_matricula = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_matricula.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_matricula.hide()
                inserir_matricula()
            
            case 'Atualizar':
                janela_menu_matricula.hide()
                atualizar_matricula()

            case 'Remover':
                janela_menu_matricula.hide()
                remove_matricula()
            
            case 'Visualizar':
                janela_menu_matricula.hide()
                visualiza_matricula()

    janela_menu_matricula.close()



def inserir_matricula():
    janela = i_matricula.inserir_matricula()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Ok'):     
            crud_matricula.inserir_matricula([values['id'],values['turma']])
           
    janela.close()

def atualizar_matricula():
    sg.popup('Remova a matricula')

def remove_matricula():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):

            crud_matricula.crud_remove_matricula(values['id'])
        
            
    
    janela.close()


def visualiza_matricula():
    valor = crud_matricula.select_matricula()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(2)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id Turma' ,'matricula'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()