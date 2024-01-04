import PySimpleGUI as sg
import random

sg.theme('black')

def obter_nome_usuario():
    layout = [
        [sg.Text('Digite seu nome:')],
        [sg.InputText(key='NOME')],
        [sg.Button('Iniciar')]
    ]

    janela_nome = sg.Window('Nome do Jogador', layout, finalize=True)

    while True:
        event, values = janela_nome.read()

        if event == sg.WIN_CLOSED or event == 'Iniciar':
            nome_usuario = values['NOME']
            break

    janela_nome.close()
    return nome_usuario

def criar_janela(pergunta_resposta):
    pergunta = pergunta_resposta["pergunta"]
    opcoes_respostas = [pergunta_resposta["resposta"]] + pergunta_resposta["incorretas"]
    random.shuffle(opcoes_respostas)

    layout = [
        [sg.Text(pergunta)],
        [sg.Button(opcao) for opcao in opcoes_respostas]
    ]

    return sg.Window('ziuQ Books', layout, finalize=True)

def main():
    perguntas_respostas = [
        {"pergunta": "Quem é o autor de 'Crepúsculo'?", "resposta": "Stephenie Meyer", "incorretas": ["Emily Bronte", "Jane Austen", "Nenhum"]},
        {"pergunta": "Quem é autor de Harry Potter?", "resposta": "J.K. Rowling", "incorretas": ["George Orwell", "Harlan Coben", "Nenhum"]},
        {"pergunta": "Quem é autor de E se eu ficar?", "resposta": "Gayle Forman", "incorretas": ["Stephenie Meyer", "J.K. Rowling", "Nenhum"]},
        {"pergunta": "Quem é autor de 1984?", "resposta": "George Orwell", "incorretas": ["Jane Austen", "Harlan Coben", "Nenhum"]},
        {"pergunta": "Quem é autor de Fique comigo?", "resposta": "Harlan Coben", "incorretas": ["George Orwell", "Stephenie Meyer", "Nenhum"]}
    ]

    nome_usuario = obter_nome_usuario()
    pontuacao_correta = 0
    pontuacao_incorreta = 0

    for pergunta_resposta in perguntas_respostas:
        janela = criar_janela(pergunta_resposta)

        while True:
            event, values = janela.read()

            if event == sg.WIN_CLOSED:
                return

            resposta_correta = pergunta_resposta["resposta"]

            if event == resposta_correta:
                sg.popup_ok('Resposta correta!')
                pontuacao_correta += 1
                break
            elif event in pergunta_resposta["incorretas"]:
                sg.popup_error('Resposta incorreta. Tente novamente.')
                pontuacao_incorreta += 1
                break

        janela.close()

    sg.popup_ok(f'Jogo concluído, {nome_usuario}! Pontuação final - Corretas: {pontuacao_correta}, Incorretas: {pontuacao_incorreta}')

if __name__ == '__main__':
    main()
