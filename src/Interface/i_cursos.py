import random 
import PySimpleGUI as sg 

from   src.Cruds import crud_cursos


def inserir_cursos():
    
    while True:
        valor = random.randint(5999,9999)
        id    = crud_cursos.condicao_existencia_cursos(valor)

        if not(id): break


    frame = [
        [
            sg.Text(f'Seu id = {valor}',font='calibri'),
            sg.Input(f'{valor}',key='id',visible=False)
        ],
        [
            sg.Text('Nome:         '),sg.Input('',key='nome')
        ],
        [
            sg.Text('Id Centro:    '),sg.Input('',key='centro')
        ],
        [
            sg.Text('Id Coordenador:'),sg.Input(key='professor',size=(42,20))
        ],
        [
            sg.Text('Carga Horaria:  '),sg.Spin([i for i in range(32,128+1)],key='carga',size=(12,20))
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

    return sg.Window('Inserir cursos',layout=layout,element_justification='c',font='calibri')


def atualiza_cursos():

    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(44,20),key='id')],
        [
            sg.Text('Nome:      '),
            sg.Input(key='nome',size=(46,20))],
        [
            sg.Text('Id centro: '),
            sg.Input("",size=(46,20),key='centro')
        ],
        [
            sg.Text('Id professor:  '),
            sg.Input(key='professor',size=(43,20))
        ],
        [
            sg.Text('Carga Horaria:'),
            sg.Input(key='carga',size=(42,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza cursos',layout=layout,element_justification='c',font='calibri')

