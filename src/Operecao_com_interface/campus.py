from src.Interface import menu
from src.Interface import i_campus

from src.Cruds import crud_campus

import PySimpleGUI as sg 

def menu_campus(dtype):
    

    while True:
        janela_menu_campus = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_campus.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_campus.hide()
                inserir_campus()
            
            case 'Atualizar':
                janela_menu_campus.hide()
                atualizar_campus()

            case 'Remover':
                janela_menu_campus.hide()
                remove_campus()
            
            case 'Visualizar':
                janela_menu_campus.hide()
                visualiza_campus()

    janela_menu_campus.close()





def inserir_campus():
    janela = i_campus.inserir_campus()

    while True:
        event , values = janela.read()
    
        if (event == 'Voltar' or event == sg.WIN_CLOSED):break

        if (event == 'Ok'):
            try:
                id = int(values['id'])
                id_reitor = int(values['reitor'])
            except Exception:
                id = reitor = 0
         
            booleano = crud_campus.inserir_campus([id,values['nome'],id_reitor,values['local']])
            if (booleano): sg.popup('Inserido')

    janela.close()




def atualizar_campus():
    janela = i_campus.atualiza_campus()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_campus.select_campus_especifico(int(values['id']))
            except ValueError:
                valores = crud_campus.select_campus_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['nome'].update(valores[1])
                janela['reitor'].update(valores[2])
                janela['local' ].update(valores[3])


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:

                    crud_campus.crud_atualiza_campus([
                        id,
                        values['nome'],
                        int(values['reitor']),
                        values['local']
                    ]
                    )
                except ValueError:
                    sg.popup('Id não é numero')

                janela['nome'].update('')
                janela['reitor'].update('')
                janela['local' ].update('')

    janela.close()




def remove_campus():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            booleano = crud_campus.crud_remove_campus(id)
        
            if (booleano): sg.popup('Removido',auto_close=True,auto_close_duration=1)
    
    janela.close()




def visualiza_campus():
    valor = crud_campus.select_campus()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(4)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

        
    janela = menu.Visualizar(
        ['Id campus' ,'nome','reitor','local campus'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()