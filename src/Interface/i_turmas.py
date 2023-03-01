import PySimpleGUI as sg 


def inserir_turmas():
    frame = [
        [
            sg.Text('Id turma:'),
            sg.Input(key='id'),
        ],
        [
            sg.Text('       Ano:'),
            sg.Combo([i for i in range(1979,2022)],default_value='2022',key='ano'),
            sg.Text(' Semestre:'),
            sg.Combo([1,2],default_value=1,key='semestre')
        ],
        [
            sg.Text('Id disciplina:'),sg.Input(key='disciplina',size=(42,20))
        ],
        [
            sg.Text('         Estado:'),
            sg.Combo(['CONCLUÍDA','ABERTA'],default_value='ABERTA',key='estado'),
            sg.Text('Id Local'),
            sg.Input(key='local',size=(20,20))
        ],
        [
            sg.Text('Horario de Inicio:'),
            sg.Combo([str(i)+':00' for i in range(8,22,2)],key='inicio',default_value='08:00'),
            sg.Text('Horario Final'),
            sg.Combo([str(i)+':00' for i in range(10,24,2)],key='final',default_value='10:00')
        ],
        [
            sg.Text('                 Vagas:'),
            sg.Combo([i for i in range(2,100)],key='vagas',size=(6,10),default_value=2),
            sg.Text('Matriculados'),
            sg.Combo([i for i in range(2,99)],key='matriculados',size=(6,10),default_value=2),
        ]
    ]
    layout = [
        [
            sg.Frame('Cadastro',layout=frame),
        ],
        [
            sg.Ok(),sg.Button('Voltar')
        ]
    ]
    return sg.Window('Inserir Turmas',layout=layout,font='calibri')


def atualiza_turmas():
    frame = [
        [
            sg.Text('Id turma:'),
            sg.Input(key='id'),
        ],
        [
            sg.Text('       Ano:'),
            sg.Combo([i for i in range(1979,2022)],default_value='2022',key='ano'),
            sg.Text(' Semestre:'),
            sg.Combo([1,2],default_value=1,key='semestre')
        ],
        [
            sg.Text('Id disciplina:'),sg.Input(key='disciplina',size=(42,20))
        ],
        [
            sg.Text('         Estado:'),
            sg.Combo(['CONCLUÍDA','ABERTA'],default_value='ABERTA'),
            sg.Text('Id Local'),
            sg.Input(key='local',size=(20,20))
        ],
        [
            sg.Text('Horario de Inicio:'),
            sg.Combo([str(i)+':00' for i in range(8,22,2)],key='inicio',default_value='08:00'),
            sg.Text('Horario Final'),
            sg.Combo([str(i)+':00' for i in range(10,24,2)],key='final',default_value='10:00')
        ],
        [
            sg.Text('                 Vagas:'),
            sg.Combo([i for i in range(2,100)],key='vagas',size=(6,10),default_value=2),
            sg.Text('Matriculados'),
            sg.Combo([i for i in range(2,99)],key='matriculados',size=(6,10),default_value=2),
        ]
    ]
    layout = [
        [
            sg.Frame('Atualiza',layout=frame),
        ],
        [
            sg.Button('Verificar'),
            sg.Button('Modificar'),
            sg.Button('Voltar',mouseover_colors='orange')
        ] 
    ]
    return sg.Window('Atualizar Turmas',layout=layout,font='calibri')


