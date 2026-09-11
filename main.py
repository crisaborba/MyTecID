import FreeSimpleGUI as sg

layout = [  [sg.Text("Qual o produto que você quer adicionar ou alterar?: ")],
            [sg.Input()],
            [sg.Button('Ok')] ]

window = sg.Window('Window Title', layout)
event, values = window.read()
print('Você vai alterar o seguinte produto: ', values[0], "! Obrigado por usar o MyTecID!")
window.close()