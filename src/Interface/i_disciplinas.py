import PySimpleGUI as sg
import random

from   src.Cruds import crud_disciplina




def inserir_disciplina():
    
    while True:
        valor = random.randint(70000,85000)
        id    = crud_disciplina.condicao_existencia_disciplina(valor)
        if not(id): break


    frame = [
        [
            sg.Text(f'Seu id = {valor}',font='calibri'),
            sg.Input(f'{valor}',key='id',visible=False)
        ],

        [
            sg.Text('Nome:'),sg.Input(key='nome')
        ],
        [
            sg.Text('Id Professor:'),sg.Input("",key='professor')
        ],
        [
            sg.Text('Ementa:'),
            sg.Input(key='ementa',size=(42,20))
        ],
        [
            sg.Text('Carga Horaria'),sg.Spin([i for i in range(32,129)],key='carga')
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

    return sg.Window('Atualiza disciplina',layout=layout,element_justification='c',font='calibri')
    


#=======================================================================================
def atualiza_disciplina():
    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(40,20),key='id')
        ],   
        [
            sg.Text('Nome:    '),sg.Input(key='nome',size=(43,20))
        ],
        [
            sg.Text('Id Professor:'),sg.Input("null",key='professor',size=(40,20))
        ],
        [
            sg.Text('Ementa:   '),
            sg.Input(key='ementa',size=(42,20))
        ],
        [
            sg.Text('Carga Horaria:'),sg.Input('',key='carga',size=(38,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza disciplina',layout=layout,element_justification='c',font='calibri')



