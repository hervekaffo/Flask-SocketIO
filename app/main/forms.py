from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a name and a Channel."""
    name = StringField('Enter your Name', validators=[Required()])
    room = StringField('Create a new channel', validators=[Required()])
    submit = SubmitField('Enter Chatroom')
