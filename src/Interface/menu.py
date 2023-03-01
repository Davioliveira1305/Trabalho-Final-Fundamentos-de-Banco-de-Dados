import psycopg2    as ps 
import PySimpleGUI as sg

txt2 = 'Quais locais estão em um dado bloco.'
def menu():
    frame1 = [
    
        [sg.Button('Reitor'    ,size=(10,1)),sg.Button('Professor' ,size=(10,1)),sg.Button('Campus'    ,size=(10,1))],
        [sg.Button('Centros'   ,size=(10,1)),sg.Button('Curso'     ,size=(10,1)),sg.Button('Prof Curso',size=(10,1))],
        [sg.Button('Aluno'     ,size=(10,1)),sg.Button('Disciplina',size=(10,1)),sg.Button('Blocos'    ,size=(10,1))],
        [sg.Button('Locais'    ,size=(10,1)),sg.Button('Turmas'    ,size=(10,1)),sg.Button('Dia_Semana',size=(10,1))],
        [sg.Button('Matriculas',size=(10,1)),sg.Button('Avaliações',size=(10,1))],
        
        [sg.Button('Conectar ao Servidor' ,size=(26,1),mouseover_colors='blue')]      
    ]


    frame2 = [
        [sg.Button('Consulta1')],
        [sg.Button('Consulta2')],
        [sg.Button('Consulta3')],
        [sg.Button('Consulta4')],
        [sg.Button('Consulta5')],
    ]


    layout = [
        [
  
            sg.Frame('Escolha a opção',frame1,title_location='n',element_justification='c',size=(320,260)),
            sg.Frame('Operecao Especial',frame2,title_location='n',element_justification='c',size=(150,270))
        ]
        ,
        [
            sg.Button('Sair',mouseover_colors='red',size=(10,1))
        ]

    ]
    return sg.Window('Menu',layout=layout,font='calibri')





def servidor():
    frame = [
        [sg.Text("Host..........: "),sg.InputText('127.0.0.1',key='host')],
        [sg.Text("DataBase..:  "),sg.InputText('',key='database')],
        [sg.Text("User..........: "),sg.InputText('postgres',key='user')],
        [sg.Text("Password..:  "),sg.InputText('',key='password')]
    ]
    layout = [
        [sg.Frame('Conectar ao postegres',frame)],
        [sg.Button("Continuar"),sg.Button('Voltar',mouseover_colors='orange')]
    ]

    return sg.Window('Servidor',layout=layout,element_justification='c',font='calibri')




def operacao_menu_geral(dtype ):

    frame = [
        [sg.Button('Inserir'  ,size=(12,1))],
        [sg.Button('Atualizar',size=(12,1))],
        [sg.Button('Remover',size=(12,1))],
        [sg.Button('Visualizar',size=(12,1))]    
    ]
    layout = [
        [sg.Frame('Escolha opcao',layout=frame,title_location='n',element_justification='c')],
        [sg.Button('Voltar',mouseover_colors='orange')]      

    ]
    return sg.Window(
        f'Menu {dtype}',
        layout=layout,
        element_justification='c',font='calibri',no_titlebar=True)




def Visualizar(colunas,valores):
    tabela = [
        [sg.Table(valores,colunas)],
        [sg.Button('Voltar')]
    ]

    return sg.Window(f'Tabela',layout=tabela,element_justification='c',font='calibri',no_titlebar=True)


def remover():
    frame = [
        [
            sg.Input('',size=(43,20),key='id')
        ]
    ]

    layout = [
        [
            sg.Frame('Insira id',frame)
        ],
        [
            sg.Button('Excluir'),
            sg.Button('Voltar',mouseover_colors='orange')
        ]
    ]
    return sg.Window(
        'Remover',
        layout=layout,
        element_justification='c',
        font='calibri',
        
        )

def consultas(valor):
    frame = [
        [
            sg.Input('',size=(43,20),key='id')
        ]
    ]

    layout = [
        [
            sg.Frame(f'{valor}: ',frame)
        ],
        [
            sg.Ok(),sg.Button('Voltar',mouseover_colors='orange')
        
        ]
    ]
    return sg.Window(
        f'{valor}',
        layout=layout,
        element_justification='c',
        font='calibri',
        
        )


def consulta5():
    frame = [
        [
            sg.Text('Ano:'),
            sg.Combo([i for i in range(1930,2022)],default_value=2020,key='ano',size=(10,1)),
        ],
        [
            sg.Text('Semestre: ',),
            sg.Combo([i for i in range(1,3)],default_value=1,key='semestre',size=(10,1))
        ]
    ]

    layout = [
        [sg.Frame('escolha',layout=frame)],
        [sg.Ok(),sg.Button('Voltar')]
    ]

    return sg.Window('Consulta5',layout=layout)
