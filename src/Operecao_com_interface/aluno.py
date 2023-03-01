import PySimpleGUI as sg


from   src.Interface import menu 
from   src.Interface import i_aluno

from   src.Cruds import crud_aluno




def menu_aluno(dtype):
    while True:
        janela_menu_prof = menu.operacao_menu_geral(dtype)    
        event , values = janela_menu_prof.read()

        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        match (event):
            case 'Inserir':
                janela_menu_prof.hide()
                inserir_aluno()
            
            case 'Atualizar':
                janela_menu_prof.hide()
                atualizar_aluno()

            case 'Remover':
                janela_menu_prof.hide()
                remove_aluno()
            
            case 'Visualizar':
                janela_menu_prof.hide()
                visualiza_aluno()

    janela_menu_prof.close()




def inserir_aluno():
  
    janela = i_aluno.inserir_aluno()

    while True:
        event , values = janela.read()
       
        if event == 'Voltar' or event == sg.WIN_CLOSED: break

        if event == 'Ok':
            try:
                id = int(values['id'])
                id_curso =  int(values['curso'])
                numero   =  int(values['numero'])
                                
                crud_aluno.inserir_alunos([
                    id,
                    id_curso,
                    values['nome'],
                    values['sobrenome'],
                    values['email'],
                    values['nascimento'],
                    values['numero'],
                    values['rua'],
                    values['bairro'],
                    values['cidade'],
                    values['estado'],
                    values['sexo']
            ])

            except Exception as e:
                sg.popup('No e inteiro',str(e))


    janela.close()



def atualizar_aluno():
    valores = id = None

    janela = i_aluno.atualiza_aluno()

    while True:
        event , values = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break

        if (event == 'Verificar'):

            try:
                valores = crud_aluno.select_alunos_especifico(int(values['id']))
            except ValueError:
                valores = crud_aluno.select_alunos_especifico(0)


            if (valores == False):
                sg.popup('Id invalido')

            else :
                id = int(valores[0])
                janela['curso'].update(valores[1])
                janela['nome'].update(valores[2])
                janela['sobrenome'].update(valores[3])
                janela['email'].update(valores[4])
                janela['nascimento'].update(valores[5])
                janela['numero'].update(valores[6])
                janela['rua'].update(valores[7])
                janela['bairro'].update(valores[4])
                janela['cidade'].update(valores[4])
                janela['estado'].update(valores[4])
                janela['sexo'].update(valores[4])

    
        if (event =='Modificar'):
            
            if (valores==None):
                sg.popup('Verifique Primeiro')

            else:
                crud_aluno.crud_atualiza_alunos([
                    id,
                    int(values['curso']),
                    values['nome'],
                    values['sobrenome'],
                    values['email'],
                    values['nascimento'],
                    values['numero'],
                    values['rua'],
                    values['bairro'],
                    values['cidade'],
                    values['estado'],
                    values['sexo']
                ]
                )
                janela['nome'].update('')
                janela['email'].update('')
                janela['formacao' ].update('')
                janela['sexo'].update('')
                janela['nascimento'].update('')
                janela['bairro'].update('')
                janela['cidade'].update('')
                janela['estado'].update('')
                janela['sexo'].update('')
                janela['rua'].update('')

    janela.close()
            
        
        
        
           
        
def remove_aluno():
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
            crud_aluno.crud_remove_alunos(id)
  
    
    janela.close()



    
    
    
def visualiza_aluno():
    valor = crud_aluno.select_alunos()


    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(6)]
        lista_valores = valor
    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Matricula' ,
        'Id curso' ,
        'Nome',
        'Sobrenome',
        'Email',
        'Data de nascimento',
        'Numero',
        'Rua',
        'Bairro',
        'Cidade',
        'Estado',
        'Sexo'],
        lista_valores)

    while True:
        event ,value = janela.read()
        if (event == 'Voltar'):break
        
    janela.close()



