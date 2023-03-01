import PySimpleGUI as sg
def inserir_reitor():
    frame =[         
            [
                sg.Text('Id:'),sg.Input(key='id')
            ],
            [
                sg.Col([
                    [
                        sg.CalendarButton(
                        'Data de Admissao', 
                            key='data admissao', 
                            format=('%Y/%m/%d'),
                            pad=None,
                            location= (900, 300),
                            close_when_date_chosen=False
                    )
                ]
                ])
            ]
        ]   
    layout = [
        [sg.Frame('Cadastro',layout=frame)],
        [
            sg.Ok(),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

    return sg.Window('Inserir Reitor',layout=layout,font='calibri')


def atualiza_reitor():

    frame = [
        [
            sg.Text('Id:'),sg.Input('',key='id')
        ],
        [
            sg.Text('Data de admissao:'),sg.Input('',key='data admissao')
        ]
    ]
    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]

