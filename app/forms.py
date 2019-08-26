from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class QuestionForm(FlaskForm):
    question = StringField('Entre ta question : ', validators=[DataRequired()])
    submit = SubmitField('Valider ma question')