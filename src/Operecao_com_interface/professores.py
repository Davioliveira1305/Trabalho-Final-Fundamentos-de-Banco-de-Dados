import PySimpleGUI as sg


from   src.Interface import menu 
from   src.Interface import i_professores

from   src.Cruds import crud_professor




def menu_professor(dtype):
    while True:
        janela_menu_prof = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_prof.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_prof.hide()
                inserir_professor()
            
            case 'Atualizar':
                janela_menu_prof.hide()
                atualizar_professor()

            case 'Remover':
                janela_menu_prof.hide()
                remove_professor()
            
            case 'Visualizar':
                janela_menu_prof.hide()
                visualiza_professor()

    janela_menu_prof.close()




def inserir_professor():
  
    janela = i_professores.inserir_professor()

    while True:
        event , values = janela.read()
       
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        if event == 'Ok':
            crud_professor.inserir_professor([
                values['id'],
                values['nome'],
                values['email'],
                values['formacao'],
                values['sexo'],
                values['data nascimento']
            ])

    janela.close()



def atualizar_professor():
    valores = id = None

    janela = i_professores.atualiza_professor()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_professor.select_professor_especifico(int(values['id']))
            except ValueError:
                valores = crud_professor.select_professor_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['nome'].update(valores[1])
                janela['email'].update(valores[2])
                janela['formacao' ].update(valores[3])
                janela['sexo'].update(valores[4])
                janela['data nascimento'].update(valores[5])

    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                crud_professor.crud_atualiza_professor([
                    id,
                    values['nome'],
                    values['email'],
                    values['formacao'],
                    values['sexo'],
                    values['data nascimento']
                ]
                )
                janela['nome'].update('')
                janela['email'].update('')
                janela['formacao' ].update('')
                janela['sexo'].update('')
                janela['data nascimento'].update('')

    janela.close()
            
        
        
        
           
        
def remove_professor():
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
            crud_professor.crud_remove_professor(id)
  
    
    janela.close()



    
    
    
def visualiza_professor():
    valor = crud_professor.select_professor()


    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(6)]
        lista_valores = valor

    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['ID_Professor' ,
        'Nome' ,
        'Email',
        'Formacao',
        'Sexo',
        'data_de_nascimento'],
        lista_valores)

    while True:
        event ,value = janela.read()
        if (event == 'Voltar'):break
        
    janela.close()



