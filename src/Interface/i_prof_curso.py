import random 
import PySimpleGUI as sg 


def inserir_prof_curso():

    frame = [
        [
            sg.Text('Id Professor:'),
            sg.Input("",size=(43,20),key='professor')
        ],
        [
            sg.Text('Id curso:'),
            sg.Input(key='curso',size=(45,20))
        ]
    ]


    layout = [
        [
            sg.Frame('Cadastro',layout=frame)
        ],
        [
            sg.Ok(),sg.Button('Voltar')
        ]
    ]

    return sg.Window('Inserir prof_curso',layout=layout,element_justification='c',font='calibri')
    



def atualiza_prof_curso():

    frame = [
        [
            sg.Text('Id Professor:'),
            sg.Input("",size=(43,20),key='professor')
        ],
        [
            sg.Text('Id curso:'),
            sg.Input(key='curso',size=(45,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza prof_curso',layout=layout,element_justification='c',font='calibri')

