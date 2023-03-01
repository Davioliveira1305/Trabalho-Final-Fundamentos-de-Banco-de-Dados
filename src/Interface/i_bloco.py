import PySimpleGUI as sg
def inserir_bloco():
    frame =[         
            [
                sg.Text('Id bloco :'),sg.Input(key='id')
            ],
            [
                sg.Text('Id centro:'),sg.Input(key='centro')
            ]
        ]   
    layout = [
        [sg.Frame('Cadastro',layout=frame)],
        [
            sg.Ok(),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

    return sg.Window('Inserir bloco',layout=layout,font='calibri')


def atualiza_bloco():

    frame = [
        [
            sg.Text('Id bloco :'),sg.Input(key='id')
        ],
        [
            sg.Text('Id centro:'),sg.Input(key='centro')
        ]
    ]
    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

