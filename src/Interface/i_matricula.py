import PySimpleGUI as sg
def inserir_matricula():
    frame =[         
            [
                sg.Text('Matricula:'),sg.Input(key='id')
            ],
            [
                sg.Text('Id Turma:'),sg.Input(key='turma')
            ]
        ]   
    layout = [
        [sg.Frame('Cadastro',layout=frame)],
        [
            sg.Ok(),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

    return sg.Window('Inserir dia_semana',layout=layout,font='calibri')


def atualiza_matricula():

    frame = [
        [
            sg.Text('Matricula:'),sg.Input('',key='id')
        ],
        [
            sg.Text('Id turma:'),sg.Input('',key='turma')
        ]
    ]
    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]