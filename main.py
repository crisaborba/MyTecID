import FreeSimpleGUI as sg

layout = [  [sg.Text("Qual o produto que você quer adicionar ou alterar?: ")],
            [sg.Input()],
            [sg.Button('Ok')] ]

window = sg.Window('Window Title', layout)
event, values = window.read()
print('Hello', values[0], "! Thanks for trying FreeSimpleGUI")
window.close()