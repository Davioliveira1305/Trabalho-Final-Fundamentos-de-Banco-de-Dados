from src.Interface import menu
from src.Interface import i_local

from src.Cruds import crud_local

import PySimpleGUI as sg 

def menu_local(dtype):
    

    while True:
        janela_menu_local = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_local.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_local.hide()
                inserir_local()
            
            case 'Atualizar':
                janela_menu_local.hide()
                atualizar_local()

            case 'Remover':
                janela_menu_local.hide()
                remove_local()
            
            case 'Visualizar':
                janela_menu_local.hide()
                visualiza_local()

    janela_menu_local.close()





def inserir_local():
    janela = i_local.inserir_local()

    while True:
        event , values = janela.read()
    
        if (event == 'Voltar' or event == sg.WIN_CLOSED):break

        if (event == 'Ok'):
         
            crud_local.inserir_local([
                        values['id'],
                        values['tipo'],
                        values['bloco'],
                        values['lotacao'],
                        values['nome'],
                        values['descricao']
                        ])
    

    janela.close()




def atualizar_local():
    janela = i_local.atualiza_local()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_local.select_local_especifico(int(values['id']))
            except ValueError:
                valores = crud_local.select_local_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['tipo'].update(valores[1])
                janela['bloco'].update(valores[2])
                janela['lotacao'].update(valores[3])
                janela['nome'].update(valores[4])
                janela['descricao'].update(valores[5])


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:

                    crud_local.crud_atualiza_local([
                        values['id'],
                        values['tipo'],
                        values['bloco'],
                        values['lotacao'],
                        values['nome'],
                        values['descricao']
                    ]
                    )
                except Exception as e:
                    sg.popup(f'{str(e)}')

                janela['tipo'].update('')
                janela['bloco'].update('')
                janela['lotacao'].update('')
                janela['nome'].update('')
                janela['descricao'].update('')

    janela.close()




def remove_local():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            booleano = crud_local.crud_remove_local(id)
        
            if (booleano): sg.popup('Removido',auto_close=True,auto_close_duration=1)
    
    janela.close()




def visualiza_local():
    valor = crud_local.select_local()
    
    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(6)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]


    janela = menu.Visualizar(
        ['Id local' ,'Tipo','Id Bloco','Lotação','Nome','Descrição'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()