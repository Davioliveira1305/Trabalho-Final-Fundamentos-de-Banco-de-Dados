import PySimpleGUI as sg
import random

from   src.Cruds import crud_aluno




def inserir_aluno(valor=1):
    
    while True:
        valor = random.randint(10000,49999)
        id    = crud_aluno.condicao_existencia_alunos(valor)
        if not(id): break


    frame = [
        [
            sg.Text(f'Seu id = {valor}',font='calibri'),
            sg.Input(f'{valor}',key='id',visible=False)
        ],
        [
            sg.Text('Id Curso:'),sg.Input('',key='curso',size=(44,20))
        ],
        [
            sg.Text('Nome:    '),sg.Input(key='nome',size=(15,20)),
            sg.Text('Sobrenome: '),sg.Input(key='sobrenome',size=(15,20))   
        ],
        [
            sg.Text('     Sexo: '),
            sg.Combo(['Feminino','Masculino'],'Feminino',key='sexo'),
            sg.Col([
                [
                    sg.CalendarButton(
                    'Data de Nascimento', 
                        key='nascimento', 
                        format=('%Y-%m-%d'),
                        pad=None,
                        location= (900, 300),
                        close_when_date_chosen=False,
                    )
                ]
                ])
        ],
        [
            sg.Text('Email:'),sg.Input("@alu.ufc.br",key='email')
        ],
        [
            sg.Text('Bairro:'),sg.Input(key='bairro'),
    
        ],
        [
            sg.Text('Rua:   '),sg.Input(key='rua',size=(15,20)),
            sg.Text('Numero: '),sg.Input(key='numero',size=(15,20))   
        ],
        [
            sg.Text('Cidade:'),sg.Input(key='cidade',size=(15,20)),
            sg.Text('Estado: '),sg.Input(key='estado',size=(15,20))   
        ],
    ]


    layout = [
        [
            sg.Frame('Cadastro',layout=frame)
        ],
        [
            sg.Ok(),sg.Button('Voltar')
        ]
    ]

    return sg.Window('Cadastro Aluno',layout=layout,element_justification='c',font='calibri')
    


#=======================================================================================
def atualiza_aluno():
    frame = [
        [
            sg.Text('Insira seu Id :'),
            sg.Input('',size=(43,20),key='id')
        ],
        [  
            sg.Text('Id curso :       '),
            sg.Input('',size=(43,20),key='curso')
        ], 
        [
            sg.Text('Nome:           '),
            sg.Input(key='nome',size=(43,20))
        ],
        [
            sg.Text('Sobrenome:  '),
            sg.Input(key='sobrenome',size=(43,20))
        ],
        [ 
            sg.Text('Email:        '),
            sg.Input("@prof.ufc.br",size=(45,20),key='email')
        ],
  
        [
            sg.Text('        Sexo: '),
            sg.Input('Feminino',key='sexo'),
            sg.Text('Data: '),
            sg.Input('',size=(15,20),key='nascimento')
        ],
        [
            sg.Text('Bairro: '),
            sg.Input(key='bairro',size=(15,20))
        ],
        [
            sg.Text('Rua:    '),
            sg.Input(key='rua',size=(15,20)),
            sg.Text('Numero:'),
            sg.Input(key='numero',size=(15,20))
        ],
        [
            sg.Text('Cidade:'),
            sg.Input(key='cidade',size=(15,20)),
            sg.Text('Estado:'),
            sg.Input(key='estado',size=(15,20))
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza Aluno',layout=layout,element_justification='c',font='calibri')


