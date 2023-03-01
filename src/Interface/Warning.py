import PySimpleGUI as sg 
def erro_i():sg.popup('Id inxistente')

def atualizado():sg.popup('Atualizado')

def removido():sg.popup('Removido')

def inserido():sg.popup('Inserido')


def get_message(value):sg.popup(f'{value}')