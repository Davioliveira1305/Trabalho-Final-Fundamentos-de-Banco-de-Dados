from src.Interface import menu
from src.Interface import i_cursos

from src.Cruds import crud_cursos

import PySimpleGUI as sg 

def menu_cursos(dtype):
    

    while True:
        janela_menu_cursos = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_cursos.read()
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_cursos.hide()
                inserir_cursos()
            
            case 'Atualizar':
                janela_menu_cursos.hide()
                atualizar_cursos()

            case 'Remover':
                janela_menu_cursos.hide()
                remove_cursos()
            
            case 'Visualizar':
                janela_menu_cursos.hide()
                visualiza_cursos()

    janela_menu_cursos.close()





def inserir_cursos():
    janela = i_cursos.inserir_cursos()

    while True:
        event , values = janela.read()
    
        if (event == 'Voltar' or event == sg.WIN_CLOSED):break

        if (event == 'Ok'):
            try:
                id = int(values['id'])
                id_centro = int(values['centro'])
                id_coord  = int(values['professor'])
                carga     = int(values['carga'])
            except Exception as e:
                id = id_centro = id_coord = carga = 0
         
            crud_cursos.inserir_cursos([id,values['nome'],id_centro,id_coord,carga])
            

    janela.close()




def atualizar_cursos():
    janela = i_cursos.atualiza_cursos()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_cursos.select_cursos_especifico(int(values['id']))
            except ValueError:
                valores = crud_cursos.select_cursos_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['nome'].update(valores[1])
                janela['centro'].update(valores[2])
                janela['professor'].update(valores[3])
                janela['carga' ].update(valores[4])


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')
            else:
                try:
                    id = int(values['id'])
                    id_centro = int(values['centro'])
                    id_coord  = int(values['professor'])
                    carga     = int(values['carga'])
                except Exception as e:
                    id = id_centro = id_coord = carga = 0
                
                crud_cursos.crud_atualiza_cursos(
                    [id,values['nome'],id_centro,id_coord,carga]
                )

    
                janela['nome'].update('')
                janela['centro'].update('')
                janela['professor'].update('')
                janela['carga' ].update('')

    janela.close()




def remove_cursos():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
        
            crud_cursos.crud_remove_cursos(id)
      
    
    janela.close()




def visualiza_cursos():
    valor = crud_cursos.select_cursos()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(5)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Id Curso ' ,'Nome','Centro','Coordenador','Carga Horaria'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()