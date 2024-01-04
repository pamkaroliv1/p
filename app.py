from flask import Flask, render_template, request, redirect

app = Flask(__name__)

perguntas_respostas = [
    {"pergunta": "Quem é o autor de 'Crepúsculo'?", "resposta": "Stephenie Meyer", "incorretas": ["Emily Bronte", "Jane Austen", "Nenhum"]},
    {"pergunta": "Quem é autor de Harry Potter?", "resposta": "J.K. Rowling",
     "incorretas": ["George Orwell", "Harlan Coben", "Nenhum"]},
    {"pergunta": "Quem é autor de E se eu ficar?", "resposta": "Gayle Forman",
     "incorretas": ["Stephenie Meyer", "J.K. Rowling", "Nenhum"]},
    {"pergunta": "Quem é autor de 1984?", "resposta": "George Orwell",
     "incorretas": ["Jane Austen", "Harlan Coben", "Nenhum"]},
    {"pergunta": "Quem é autor de Fique comigo?", "resposta": "Harlan Coben",
     "incorretas": ["George Orwell", "Stephenie Meyer", "Nenhum"]}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jogo', methods=['POST'])
def jogo():
    nome_usuario = request.form.get('NOME')  # Use request.form.get() para evitar KeyError
    if nome_usuario:
        return f'Nome do usuário: {nome_usuario}'
    else:
        return 'Nome do usuário não fornecido'

if __name__ == '__main__':
    app.run(debug=True)
