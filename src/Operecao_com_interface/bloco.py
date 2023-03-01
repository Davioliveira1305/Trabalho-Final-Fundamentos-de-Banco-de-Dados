from src.Interface import menu
from src.Interface import i_bloco

from src.Cruds import crud_bloco

import PySimpleGUI as sg 


def menu_bloco(dtype):
    
    while True:
        janela_menu_bloco = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_bloco.read()
        
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_bloco.hide()
                inserir_bloco()
            
            case 'Atualizar':
                janela_menu_bloco.hide()
                atualizar_bloco()

            case 'Remover':
                janela_menu_bloco.hide()
                remove_bloco()
            
            case 'Visualizar':
                janela_menu_bloco.hide()
                visualiza_bloco()

    janela_menu_bloco.close()



def inserir_bloco():
    janela = i_bloco.inserir_bloco()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Ok'):
        
         
            crud_bloco.inserir_bloco([values['id'],values['centro']])
           
    janela.close()



def atualizar_bloco():
    sg.popup('Remova Blocos primeiro')



def remove_bloco():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):    
            crud_bloco.crud_remove_bloco(values['id'])
            
    janela.close()




def visualiza_bloco():
    valor = crud_bloco.select_bloco()
    
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(2)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id bloco' ,'Centro'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()
