import FreeSimpleGUI as sg

sg.theme('DarkBlue3') # Introduzir temas aumenta o engajamento visual

dados_tabela = []
cabecalhos = ['Nome', 'Telefone', 'Email', 'Cidade']

layout = [
    [sg.Text("Nome:", size=(8, 1)), sg.Input(key="-NOME-")],
    [sg.Text("Telefone:", size=(8, 1)), sg.Input(key="-TELEFONE-")],
    [sg.Text("Email:", size=(8, 1)), sg.Input(key="-EMAIL-")],
    [sg.Text("Cidade:", size=(8, 1)), sg.Input(key="-CIDADE-")],
    [sg.Button("Cadastrar"), sg.Button("Limpar"), sg.Button("Sair")],
    [sg.HorizontalSeparator()],
    # Tabela para exibir os dados armazenados
    [sg.Table(values=dados_tabela, headings=cabecalhos, max_col_width=25,
              auto_size_columns=True, justification='center', num_rows=10, key='-TABELA-')]
]

janela = sg.Window("Sistema de Cadastro de Clientes", layout)

while True:
    evento, valores = janela.read()

    if evento in (sg.WINDOW_CLOSED, "Sair"):
        break

    if evento == "Cadastrar":
        # Validação simples
        if not all([valores["-NOME-"], valores["-TELEFONE-"]]):
            sg.popup_error("Nome e Telefone são obrigatórios!")
            continue

        # Adiciona à estrutura de dados
        novo_registro = [valores["-NOME-"], valores["-TELEFONE-"], valores["-EMAIL-"], valores["-CIDADE-"]]
        dados_tabela.append(novo_registro)
        
        # Atualiza a interface
        janela['-TABELA-'].update(values=dados_tabela)
        sg.popup_ok("Cadastro inserido na tabela!")

    if evento == "Limpar":
        for key in ["-NOME-", "-TELEFONE-", "-EMAIL-", "-CIDADE-"]:
            janela[key].update("")

janela.close()