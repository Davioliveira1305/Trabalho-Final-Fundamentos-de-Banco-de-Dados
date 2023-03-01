import PySimpleGUI as sg


from   src.Interface import menu 
from   src.Interface import i_disciplinas
from   src.Interface import Warning
from   src.Cruds import crud_disciplina




def menu_disciplina(dtype):
    while True:
        janela_menu_prof = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_prof.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_prof.hide()
                inserir_disciplina()
            
            case 'Atualizar':
                janela_menu_prof.hide()
                atualizar_disciplina()

            case 'Remover':
                janela_menu_prof.hide()
                remove_disciplina()
            
            case 'Visualizar':
                janela_menu_prof.hide()
                visualiza_disciplina()

    janela_menu_prof.close()




def inserir_disciplina():
  
    janela = i_disciplinas.inserir_disciplina()

    while True:
        event , values = janela.read()
       
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        if event == 'Ok':
            crud_disciplina.inserir_disciplina([
                values['id'],
                values['nome'],
                values['professor'],
                values['ementa'],
                values['carga']    
            ])

    janela.close()



def atualizar_disciplina():
    valores = id = None

    janela = i_disciplinas.atualiza_disciplina()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_disciplina.select_disciplina_especifico(int(values['id']))
            except ValueError:
                valores = crud_disciplina.select_disciplina_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['nome'].update(valores[1])
                janela['professor'].update(valores[2])
                janela['ementa' ].update(valores[3])
                janela['carga'].update(valores[4])
 

    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                try:
                    crud_disciplina.crud_atualiza_disciplina([
                        id,
                        values['nome'],
                        int(values['professor']),
                        values['ementa'],
                        int(values['carga']),
                    
                    ]
                    )
                    janela['nome'].update('')
                    janela['professor'].update('')
                    janela['ementa' ].update('')
                    janela['carga'].update('')
                except Exception as e:
                    Warning.get_message(str(e))
      

    janela.close()
            
        
        
        
           
        
def remove_disciplina():
    id = None
    
    janela = menu.remover()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break
        if (event == 'Excluir'):
            try:
                id = int(values['id'])
            except Exception:
                id = 0            
            crud_disciplina.crud_remove_disciplina(id)
  
    
    janela.close()



    
    
    
def visualiza_disciplina():
    valor = crud_disciplina.select_disciplina()

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(4)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]


    janela = menu.Visualizar(
        ['ID_disciplina' ,
        'Nome' ,
        'Id Professor',
        'Ementa',
        'Carga Horaria'],
        lista_valores)

    while True:
        event ,value = janela.read()
        if (event == 'Voltar'):break
        
    janela.close()



