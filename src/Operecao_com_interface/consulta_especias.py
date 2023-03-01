from  src.Interface import menu
from  src.consultas_especiais import consultas

def consulta_1():
    valor = consultas.visualizar_media()
    

    if (type(valor)==bool or valor == None): 
        valor = ['' for i in range(3)]
        lista_valores = valor

    else:
        lista_valores = [list(i) for i in valor]

    janela = menu.Visualizar(
        ['Matricula','Id Disciplina', 'Media'],
        lista_valores)

    while True:
        event ,value = janela.read()
    
        if (event == 'Voltar'):break
        
    janela.close()