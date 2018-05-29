from wtforms import Form
from wtforms import StringField, TextField, PasswordField
from wtforms import validators
from Database import *
class CommentForm(Form):
	username = StringField('Usuario', 
		[
		validators.Required(message = 'El username es requerido'),
		validators.length(min=4, max=20, message='Ingrese un username válido')
		]
		)
	password = PasswordField('Contraseña', 
		[
		validators.Required(message = 'La contraseña es requerida'),
		]
		)

