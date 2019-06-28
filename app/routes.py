from app import app
from app.models import model
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/piglatinify', methods=['POST'])
def piglatinify():
    userdata = dict(request.form)

    english_sentence = userdata['inputsentence']
    piglatin_sentence = model.piglatinify(english_sentence)

    return render_template('piglatinify.html', english_sentence=english_sentence, piglatin_sentence=piglatin_sentence)
