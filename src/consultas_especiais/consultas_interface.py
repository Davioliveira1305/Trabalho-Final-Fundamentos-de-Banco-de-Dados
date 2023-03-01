import PySimpleGUI as sg

from src.consultas_especiais import consultas as c
from  src.Interface import menu


def consulta2():
    janela = menu.consultas('Localizacao')

    while True:
        event , value = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if (event == 'Ok'):
            valor = c.localizacao(value['id'])
            
            if (type(valor)==bool or valor == None): 
                valor = ['' for i in range(2)]
                lista_valores = valor
            else:
                lista_valores = [list(i) for i in valor]
            
            janela2 = menu.Visualizar(
                ['Id local' ,'Nome'],
                lista_valores)

            while True:
                event ,value = janela2.read()
            
                if (event == 'Voltar'):break
    
            janela2.close()
    janela.close()




def consulta3():
    janela = menu.consultas('Turmas Id')

    while True:
        event , value = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if (event == 'Ok'):
            valor = c.turmas(value['id'])
            
            if (type(valor)==bool or valor==None): 
                valor = ['' for i in range(4)]
                lista_valores = valor
            else:
                lista_valores = [list(i) for i in valor]
            

            janela2 = menu.Visualizar(
                ['ID_Turma', 'Nome','Horario_inicio','Horario_Fim'],
                lista_valores)

            while True:
                event ,value = janela2.read()
            
                if (event == 'Voltar'):break
    
            janela2.close()
    janela.close()



def consulta4():
    janela = menu.consultas('Id aluno para a media')

    while True:
        event , value = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if (event == 'Ok'):
            valor = c.medias_aluno(value['id'])
            
            if (type(valor)==bool or valor==None): 
                valor = ['' for i in range(3)]
                lista_valores = valor
            else:
                lista_valores = [list(i) for i in valor]
            
            
            janela2 = menu.Visualizar(
                ['matricula','ID_Disciplina', 'Media'],
                lista_valores)

            while True:
                event ,value = janela2.read()
            
                if (event == 'Voltar'):break
    
            janela2.close()
    janela.close()



def consulta5():
    janela = menu.consulta5()

    while True:
        event , value = janela.read()

        if (event == 'Voltar' or event == sg.WIN_CLOSED): break
        
        if (event == 'Ok'):
            valor = c.historico([value['ano'],value['semestre']])
            
            if (type(valor)==bool or valor==None): 
                valor = ['' for i in range(2)]
                lista_valores = valor
            else:
                lista_valores = [list(i) for i in valor]
            
            
            janela2 = menu.Visualizar(
                ['Ano','Semestre'],
                lista_valores)

            while True:
                event ,value = janela2.read()
            
                if (event == 'Voltar'):break
    
            janela2.close()
    janela.close()

