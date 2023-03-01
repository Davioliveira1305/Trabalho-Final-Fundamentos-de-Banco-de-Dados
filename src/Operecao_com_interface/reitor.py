from src.Interface import menu
from src.Interface import i_reitor

from src.Cruds import crud_reitor
from src.Cruds import crud_professor

import PySimpleGUI as sg 

def menu_reitor(dtype):
    

    while True:
        janela_menu_reitor = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_reitor.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_reitor.hide()
                inserir_reitor()
            
            case 'Atualizar':
                janela_menu_reitor.hide()
                atualizar_reitor()

            case 'Remover':
                janela_menu_reitor.hide()
                remove_reitor()
            
            case 'Visualizar':
                janela_menu_reitor.hide()
                visualiza_reitor()

    janela_menu_reitor.close()



def inserir_reitor():
    janela = i_reitor.inserir_reitor()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Ok'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
         
            crud_reitor.inserir_reitor([id,values['data admissao']])
           
    janela.close()

def atualizar_reitor():
    sg.popup('Remova reitor')

def remove_reitor():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            crud_reitor.crud_remove_reitor(id)
        
            
    
    janela.close()


def visualiza_reitor():
    valor = crud_reitor.select_reitor()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(2)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id Reitor' ,'Data de admissao'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()