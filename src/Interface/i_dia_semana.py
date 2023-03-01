import PySimpleGUI as sg
def inserir_dia_semana():
    frame =[         
            [
                sg.Text('Id Turma:'),sg.Input(key='id')
            ],
            [
                sg.Text('Dia Semana:'),sg.Input(key='dia')
            ]
        ]   
    layout = [
        [sg.Frame('Cadastro',layout=frame)],
        [
            sg.Ok(),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

    return sg.Window('Inserir dia_semana',layout=layout,font='calibri')


def atualiza_dia_semana():

    frame = [
        [
            sg.Text('Id turma:'),sg.Input('',key='id')
        ],
        [
            sg.Text('Dia:'),sg.Input('',key='dia')
        ]
    ]
    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]


def remover():
    frame = [
        [
            sg.Text('Id:'),sg.Input('',size=(43,20),key='id')
        ],
        [
            sg.Text('Dia:'),sg.Input('',size=(43,20),key='dia')
        ]
    ]

    layout = [
        [
            sg.Frame('Insira id',frame)
        ],
        [
            sg.Button('Excluir'),
            sg.Button('Voltar',mouseover_colors='orange')
        ]
    ]
    return sg.Window(
        'Remover',
        layout=layout,
        element_justification='c',
        font='calibri'
    )