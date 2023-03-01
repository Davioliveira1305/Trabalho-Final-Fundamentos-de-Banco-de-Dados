import random 
import PySimpleGUI as sg 

from src.Cruds import crud_local


def atualiza_local():

    frame = [
        [
            sg.Text('Id  local:'),
            sg.Input('',size=(40,20),key='id')],
        [
            sg.Text('      Tipo:'),
            sg.Combo(['Bloco','Auditório','Sala de Aula','Laboratório','null'],'null',key='tipo')
        ],
        [
            sg.Text('Id Bloco:'),
            sg.Input("",size=(40,20),key='bloco')
        ],
        [
            sg.Text('Lotacao:'),
            sg.Input(key='lotacao',size=(40,20))
        ],
        [
            sg.Text('Nome:   '),
            sg.Input(key='nome',size=(40,20))
        ],
        [
            sg.Text('Descricao:'),
            sg.Input(key='descricao',size=(38,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualiza',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Local',layout=layout,element_justification='c',font='calibri')

def inserir_local():

    frame = [
        [
            sg.Text('Id  local:'),
            sg.Input('',size=(40,20),key='id')],
        [
            sg.Text('      Tipo:'),
            sg.Combo(['Bloco','Auditório','Sala de Aula','Laboratório','null'],'null',key='tipo')
        ],
        [
            sg.Text('Id Bloco:'),
            sg.Input("",size=(40,20),key='bloco')
        ],
        [
            sg.Text('Lotacao:'),
            sg.Input(key='lotacao',size=(40,20))
        ],
        [
            sg.Text('Nome:   '),
            sg.Input(key='nome',size=(40,20))
        ],
        [
            sg.Text('Descricao:'),
            sg.Input(key='descricao',size=(38,20))
        ]
    ]

    layout = [
        [sg.Frame('Cadastro',layout=frame)],
        [

            sg.Ok(),
            sg.Button('Voltar',mouseover_colors='orange')
            ]
    ]



    return sg.Window('Local',layout=layout,element_justification='c',font='calibri')