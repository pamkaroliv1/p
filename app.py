from flask import Flask, render_template, request, redirect
import PySimpleGUI as sg
import random

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jogo', methods=['POST'])
def jogo():
    nome_usuario = request.form['NOME']

    perguntas_respostas = [
        {"pergunta": "Quem é o autor de 'Crepúsculo'?", "resposta": "Stephenie Meyer",
         "incorretas": ["Emily Bronte", "Jane Austen", "Nenhum"]},
        {"pergunta": "Quem é autor de Harry Potter?", "resposta": "J.K. Rowling",
         "incorretas": ["George Orwell", "Harlan Coben", "Nenhum"]},
        {"pergunta": "Quem é autor de E se eu ficar?", "resposta": "Gayle Forman",
         "incorretas": ["Stephenie Meyer", "J.K. Rowling", "Nenhum"]},
        {"pergunta": "Quem é autor de 1984?", "resposta": "George Orwell",
         "incorretas": ["Jane Austen", "Harlan Coben", "Nenhum"]},
        {"pergunta": "Quem é autor de Fique comigo?", "resposta": "Harlan Coben",
         "incorretas": ["George Orwell", "Stephenie Meyer", "Nenhum"]}
    ]

    pontuacao_correta = 0
    pontuacao_incorreta = 0

    for pergunta_resposta in perguntas_respostas:
        pergunta = pergunta_resposta["pergunta"]
        resposta_correta = pergunta_resposta["resposta"]
        opcoes_respostas = [resposta_correta] + random.sample(pergunta_resposta["incorretas"], 2)
        random.shuffle(opcoes_respostas)

        while True:
            resposta_usuario = sg.popup_get_choice(f'{pergunta}\nEscolha a resposta:', opcoes_respostas)

            if resposta_usuario is None:
                return redirect('/')

            if resposta_usuario == resposta_correta:
                sg.popup_ok('Resposta correta!')
                pontuacao_correta += 1
                break
            else:
                sg.popup_error('Resposta incorreta. Tente novamente.')
                pontuacao_incorreta += 1

    sg.popup_ok(
        f'Jogo concluído, {nome_usuario}! Pontuação final - Corretas: {pontuacao_correta}, Incorretas: {pontuacao_incorreta}')
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)



