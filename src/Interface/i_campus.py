import random 
import PySimpleGUI as sg 

from src.Cruds import crud_campus


def inserir_campus():
    
    while True:
        valor = random.randint(1000,5999)
        id    = crud_campus.condicao_existencia_campus(valor)
        if not(id): break


    frame = [
        [
            sg.Text(f'Seu id = {valor}',font='calibri'),
            sg.Input(f'{valor}',key='id',visible=False)
        ],

        [
            sg.Text('Nome :'),sg.Input(key='nome',size=(42,20))
        ],
        [
            sg.Text('Id reitor:'),sg.Input("",key='reitor',size=(41,20))
        ],
        [
            sg.Text('Local:'),
            sg.Input(key='local',size=(43,20))
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

    return sg.Window('Inserir Campus',layout=layout,element_justification='c',font='calibri')
    



def atualiza_campus():

    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(40,20),key='id')],
        [
            sg.Text('Nome:'),
            sg.Input(key='nome',size=(45,20))],
        [
            sg.Text('Id Reitor:'),
            sg.Input("",size=(43,20),key='reitor')
        ],
        [
            sg.Text('Local :'),
            sg.Input(key='local',size=(45,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza Campus',layout=layout,element_justification='c',font='calibri')

