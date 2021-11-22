# project/server/main/forms.py


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(),
            Length(min=6, max=40)
        ],
        render_kw={'placeholder': 'Enter your email...'}
    )
    submit = SubmitField('Register!')
