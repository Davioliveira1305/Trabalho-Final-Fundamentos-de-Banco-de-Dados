
import PySimpleGUI as sg 

from src.Interface import menu
from src.Interface import i_avaliacoes
from src.Cruds     import crud_avaliacoes


def menu_avaliacoes(dtype):
    

    while True:
        janela_menu_avaliacoes = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_avaliacoes.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_avaliacoes.hide()
                inserir_avaliacoes()
            
            case 'Atualizar':
                janela_menu_avaliacoes.hide()
                atualizar_avaliacoes()

            case 'Remover':
                janela_menu_avaliacoes.hide()
                remove_avaliacoes()
            
            case 'Visualizar':
                janela_menu_avaliacoes.hide()
                visualiza_avaliacoes()

    janela_menu_avaliacoes.close()





def inserir_avaliacoes():
    janela = i_avaliacoes.inserir_avalicoes()

    while True:
        event , values = janela.read()
    
        if (event == 'Voltar' or event == sg.WIN_CLOSED):break

        if (event == 'Ok'):
            try:
                id = int(values['id'])
                
            except Exception:
                id = 0
         
            crud_avaliacoes.inserir_avaliacoes([id,values['tipo'],values['disciplina'],values['nota']])
           

    janela.close()




def atualizar_avaliacoes():
    janela = i_avaliacoes.atualiza_avalicoes()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_avaliacoes.select_avaliacoes_especifico(int(values['id']))
            except ValueError:
                valores = crud_avaliacoes.select_avaliacoes_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['tipo'].update(valores[1])
                janela['disciplina'].update(valores[2])
                janela['nota' ].update(valores[3])
                


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:

                    crud_avaliacoes.crud_atualiza_avaliacoes([
                        id,
                        values['tipo'],
                        int(values['disciplina']),
                        int(values['nota'])
                    ]
                    )
                except ValueError:
                    sg.popup('Id não é numero')

                janela['tipo'].update('')
                janela['disciplina'].update('')
                janela['nota' ].update('')

    janela.close()




def remove_avaliacoes():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            crud_avaliacoes.crud_remove_avaliacoes(id)
        

    
    janela.close()




def visualiza_avaliacoes():
    valor = crud_avaliacoes.select_avaliacoes()

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(4)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Matricula' ,'Tipo','Id disciplina','Nota'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()