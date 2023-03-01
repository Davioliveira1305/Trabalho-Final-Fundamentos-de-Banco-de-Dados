import PySimpleGUI as sg


from   src.Interface import menu 
from   src.Interface import i_turmas

from   src.Cruds import crud_turmas




def menu_turmas(dtype):
    while True:
        janela_menu_prof = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_prof.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_prof.hide()
                inserir_turmas()
            
            case 'Atualizar':
                janela_menu_prof.hide()
                atualizar_turmas()

            case 'Remover':
                janela_menu_prof.hide()
                remove_turmas()
            
            case 'Visualizar':
                janela_menu_prof.hide()
                visualiza_turmas()

    janela_menu_prof.close()




def inserir_turmas():
  
    janela = i_turmas.inserir_turmas()

    while True:
        event , values = janela.read()
       
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        if event == 'Ok':
            crud_turmas.inserir_turmas([
                values['id'],
                values['ano'],
                values['semestre'],
                values['disciplina'],
                values['estado'],
                values['local'],
                values['inicio'],
                values['final'],
                values['vagas'],
                values['matriculados']
            ])

    janela.close()



def atualizar_turmas():
    valores = id = None

    janela = i_turmas.atualiza_turmas()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_turmas.select_turmas_especifico(int(values['id']))
            except ValueError:
                valores = crud_turmas.select_turmas_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['ano'].update(valores[1])
                janela['semestre'].update(valores[2])
                janela['disciplina'].update(valores[3])
                janela['local'].update(valores[4])
                janela['inicio'].update(valores[5])
                janela['final'].update(valores[6])
                janela['vagas'].update(valores[7])
                janela['matriculados'].update(valores[8])

    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                crud_turmas.crud_atualiza_turmas([
                    id,
                    values['ano'],
                    values['semestre'],
                    values['disciplina'],
                    values['estado'],
                    values['local'],
                    values['inicio'],
                    values['final'],
                    values['vagas'],
                    values['matriculados']
                ]
                )
                janela['id'].update('')
                janela['ano'].update('')
                janela['semestre'].update('')
                janela['disciplina'].update('')
                janela['local'].update('')
                janela['inicio'].update('')
                janela['final'].update('')
                janela['vagas'].update('')
                janela['matriculados'].update('')

    janela.close()
            
        
        
        
           
        
def remove_turmas():
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
            crud_turmas.crud_remove_turmas(id)
  
    
    janela.close()



    
    
    
def visualiza_turmas():
    valor = crud_turmas.select_turmas()

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(6)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['ID_turmas' ,
        'Ano' ,
        'Semestre',
        'Id Disciplina',      
        'Estado'       ,
        'Local'        ,
        'Horario_Inicio' ,
        'Horario_Fim'    ,
        'Vagas'          ,
        'Qtde_Matriculados'],
        lista_valores)

    while True:
        event ,value = janela.read()
        if (event == 'Voltar'):break
        
    janela.close()



