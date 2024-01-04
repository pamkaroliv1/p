from flask import Flask, render_template, request, redirect

app = Flask(__name__)

perguntas_respostas = [
    {"pergunta": "Quem é o autor de 'Crepúsculo'?", "resposta": "Stephenie Meyer",
     "incorretas": ["Emily Bronte", "Jane Austen", "Nenhum"]},
    # Adicione mais perguntas aqui
]


@app.route('/')
def index():
    return render_template('index.html', perguntas_respostas=perguntas_respostas)


if __name__ == '__main__':
    app.run(debug=True)


