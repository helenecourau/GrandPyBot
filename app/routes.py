from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import QuestionForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = QuestionForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
              form.question.data))
        return redirect(url_for('index'))
    return render_template('index.html', title='Pose des questions à GrandPy !', form=form)