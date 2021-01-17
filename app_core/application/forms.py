from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class GenerateCharachterForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired()])
    second_name = StringField('Second Name', validators=[DataRequired()])
    submit = SubmitField('Generate')