import random 
import PySimpleGUI as sg 




def inserir_avalicoes():
    
    frame = [
        [
            sg.Text(f'Matricula: '),
            sg.Input(key='id')
        ],
        [
            sg.Text('Tipo:    '),sg.Input('',key='tipo')
        ],
        [
            sg.Text('Id disciplina:'),sg.Input('null',key='disciplina',size=(41,20))
        ],
        [
            sg.Text('Nota :  '),sg.Combo([i for i in range(11)],default_value=5,size=(40,20),key='nota')
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

    return sg.Window('Inserir Avaliações',layout=layout,element_justification='c',font='calibri')




def atualiza_avalicoes():

    frame = [
        [
            sg.Text(f'Insira id: '),
            sg.Input(key='id')
        ],
        [
            sg.Text('Tipo: '),sg.Input('',key='tipo',size=(48,20))
        ],
        [
            sg.Text('Id disciplina:'),sg.Input('null',key='disciplina',size=(42,20))
        ],
        [
            sg.Text('Nota :  '),sg.Combo([i for i in range(11)],default_value=5,size=(40,20),key='nota')
        ]
    ]

    layout = [
        [sg.Frame('Atualizando',layout=frame)],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')]
    ]



    return sg.Window('Atualiza Avaliações',layout=layout,element_justification='c',font='calibri')

