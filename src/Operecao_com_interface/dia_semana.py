from src.Interface import menu
from src.Interface import i_dia_semana

from src.Cruds import crud_dia_semana
from src.Cruds import crud_professor

import PySimpleGUI as sg 

def menu_dia_semana(dtype):
    

    while True:
        janela_menu_dia_semana = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_dia_semana.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_dia_semana.hide()
                inserir_dia_semana()
            
            case 'Atualizar':
                janela_menu_dia_semana.hide()
                atualizar_dia_semana()

            case 'Remover':
                janela_menu_dia_semana.hide()
                remove_dia_semana()
            
            case 'Visualizar':
                janela_menu_dia_semana.hide()
                visualiza_dia_semana()

    janela_menu_dia_semana.close()



def inserir_dia_semana():
    janela = i_dia_semana.inserir_dia_semana()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Ok'):     
            crud_dia_semana.inserir_dia([values['id'],values['dia']])
           
    janela.close()

def atualizar_dia_semana():
    sg.popup('Remova dia semana')

def remove_dia_semana():
    janela = i_dia_semana.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):

            crud_dia_semana.crud_remove_dia(values['id'],values['dia'])
        
            
    
    janela.close()


def visualiza_dia_semana():
    valor = crud_dia_semana.select_dia()

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(2)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id Turma' ,'Dia'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()