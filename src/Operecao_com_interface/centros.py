from src.Interface import menu
from src.Interface import i_centros

from src.Cruds import crud_centros

import PySimpleGUI as sg 

def menu_centros(dtype):
    

    while True:
        janela_menu_centros = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_centros.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_centros.hide()
                inserir_centros()
            
            case 'Atualizar':
                janela_menu_centros.hide()
                atualizar_centros()

            case 'Remover':
                janela_menu_centros.hide()
                remove_centros()
            
            case 'Visualizar':
                janela_menu_centros.hide()
                visualiza_centros()

    janela_menu_centros.close()





def inserir_centros():
    janela = i_centros.inserir_centros()

    while True:
        event , values = janela.read()
    
        if (event == 'Voltar' or event == sg.WIN_CLOSED):break

        if (event == 'Ok'):
            try:
                id = int(values['id'])
                if values['diretor'].lower() =='null' or values['diretor'].lower() == 'none': id_reitor = 'null'
                else:                           id_reitor = int(values['diretor'])
            except Exception:
                id = reitor = 0
         
            booleano = crud_centros.inserir_centros([id,values['nome'],id_reitor,values['campus']])
            if (booleano): sg.popup('Inserido')

    janela.close()




def atualizar_centros():
    janela = i_centros.atualiza_centros()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_centros.select_centros_especifico(int(values['id']))
            except ValueError:
                valores = crud_centros.select_centros_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['nome'].update(valores[1])
                janela['diretor'].update(valores[2])
                janela['campus' ].update(valores[3])
                


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:

                    crud_centros.crud_atualiza_centros([
                        id,
                        values['nome'],
                        int(values['diretor']),
                        int(values['campus'])
                    ]
                    )
                except ValueError:
                    sg.popup('Id não é numero')

                janela['nome'].update('')
                janela['reitor'].update('')
                janela['campus' ].update('')

    janela.close()




def remove_centros():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            crud_centros.crud_remove_centros(id)
        

    
    janela.close()




def visualiza_centros():
    valor = crud_centros.select_centros()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(4)]
        lista_valores = valor

    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id centro ' ,'nome','Diretor','Local Campus'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()