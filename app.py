import PySimpleGUI as sg


# Criando Layout
layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')]  
]


# Adicionando layout em uma janela
window = sg.Window('Login', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario_correto = 'vito'
        senha_correta = '123456'
        usuario = values['usuario']
        senha = values['senha']
        if usuario == usuario_correto and senha == senha_correta:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha incorreta')