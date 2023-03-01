import random 
import PySimpleGUI as sg 

from   src.Cruds import crud_centros


def inserir_centros():
    
    while True:
        valor = random.randint(0,99)
        id    = crud_centros.condicao_existencia_centros(valor)

        if not(id): break


    frame = [
        [
            sg.Text(f'Seu id = {valor}',font='calibri'),
            sg.Input(f'{valor}',key='id',visible=False)
        ],
        [
            sg.Text('Nome:'),sg.Input('',key='nome')
        ],
        [
            sg.Text('Id diretor:'),sg.Input('null',key='diretor',size=(42,20))
        ],
        [
            sg.Text('Id campus :'),sg.Input(key='campus',size=(41,20))
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

    return sg.Window('Inserir Centros',layout=layout,element_justification='c',font='calibri')


def atualiza_centros():

    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(44,20),key='id')],
        [
            sg.Text('Nome: '),
            sg.Input(key='nome',size=(49,20))],
        [
            sg.Text('Id diretor: '),
            sg.Input("",size=(46,20),key='diretor')
        ],
        [
            sg.Text('Id campus : '),
            sg.Input(key='campus',size=(45,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza Centros',layout=layout,element_justification='c',font='calibri')

