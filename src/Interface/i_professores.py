import PySimpleGUI as sg
import random

from   src.Cruds import crud_professor




def inserir_professor():
    
    while True:
        valor = random.randint(100,999)
        id    = crud_professor.condicao_existencia_professor(valor)
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
            sg.Text('Email:'),sg.Input("@prof.ufc.br",key='email')
        ],
        [
            sg.Text('Formação'),
            sg.Input(key='formacao',size=(42,20))
        ],
        [
            sg.Text('Sexo: '),
            sg.Combo(['Feminino','Masculino'],'Feminino',key='sexo')
        ],
        [
            sg.Col([
                [
                    sg.CalendarButton(
                    'Data de Nascimento', 
                        key='data nascimento', 
                        format=('%Y/%m/%d'),
                        pad=None,
                        location= (900, 300),
                        close_when_date_chosen=False,
                    )
                ]
                ])
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

    return sg.Window('Inserir Professor',layout=layout,element_justification='c',font='calibri')
    


#=======================================================================================
def atualiza_professor():
    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(43,20),key='id')],
        [
            sg.Text('Nome:       '),
            sg.Input(key='nome')],
        [
            sg.Text('Email:       '),
            sg.Input("@prof.ufc.br",size=(45,20),key='email')
        ],
        [
            sg.Text('Formação:'),
            sg.Input(key='formacao',size=(45,20))
        ],
        [
            sg.Text('Sexo: '),
            sg.Combo(['Feminino','Masculino'],'Feminino',key='sexo')
        ],
        [
            sg.Text('Data: '),
            sg.Input('',size=(13,20),key='data nascimento')
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')
        ]
    ]



    return sg.Window('Atualiza Professor',layout=layout,element_justification='c',font='calibri')



