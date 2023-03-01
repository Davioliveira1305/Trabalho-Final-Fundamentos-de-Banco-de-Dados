from src.Interface import menu
from src.Interface import i_prof_curso
from src.Cruds import crud_prof_curso

import PySimpleGUI as sg 

def menu_prof_curso(dtype):
    

    while True:
        janela_menu_prof_curso = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_prof_curso.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_prof_curso.hide()
                inserir_prof_curso()
            
            case 'Atualizar':
                janela_menu_prof_curso.hide()
                atualizar_prof_curso()

            case 'Remover':
                janela_menu_prof_curso.hide()
                remove_prof_curso()
            
            case 'Visualizar':
                janela_menu_prof_curso.hide()
                visualiza_prof_curso()

    janela_menu_prof_curso.close()



def inserir_prof_curso():
    janela = i_prof_curso.inserir_prof_curso()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED):break
        if (event == 'Ok'):
            try:
                id_prof  = int(values['professor'])
                id_curso = int(values['curso'])
            except Exception:
                id_prof = id_curso = 0

            crud_prof_curso.inserir_prof_curso([id_prof,id_curso])
           
    janela.close()



def atualizar_prof_curso():
    janela = i_prof_curso.atualiza_prof_curso()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_prof_curso.select_prof_curso_especifico(int(values['professor']))
            except ValueError:
                valores = crud_prof_curso.select_prof_curso_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
            
                id = int(valores[0])
                janela['curso'].update(valores[1])
   


    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:
                    prof  = values['professor']
                    curso = values['curso'] 
                    crud_prof_curso.crud_atualiza_prof_curso([
                        prof,
                        curso
                    ]
                    )
                except ValueError:
                    sg.popup('Id não é numero')

                janela['professor'].update('')
                janela['curso'].update('')
              

    janela.close()


def remove_prof_curso():
    janela = menu.remover()

    while True:
        event , values = janela.read()
        
        if ( event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if ( event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0
                
            crud_prof_curso.crud_remove_prof_curso(id)
        
            
    
    janela.close()


def visualiza_prof_curso():
    valor = crud_prof_curso.select_prof_curso()
 
    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(2)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    
    janela = menu.Visualizar(
        ['Id Professor' ,'Id curso'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()