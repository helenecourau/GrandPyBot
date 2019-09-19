'''This the file to run the project and define routes'''
from flask import Flask, render_template, jsonify, request


from backend import main as m

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    '''Display homepage'''
    return render_template('index.html',
                           title='Pose des questions à GrandPy !')


@app.route('/process', methods=['POST'])
def process():
    '''Send the data after parsing and requesrings APIs'''
    if request.form['question']:
        user_question = request.form['question']
        parse = m.ParseRequest()
        parse.script(user_question)
        return jsonify({'lat': parse.lat,
                        'lng': parse.lng,
                        'title': parse.title,
                        'description': parse.description,
                        'url': parse.url,
                        'adress': parse.adress,
                        'random_sentence': parse.random_sentence})

    return jsonify({'error': 'Le champ ne peut pas être vide'})


if __name__ == '__main__':
    app.run(debug=True)
