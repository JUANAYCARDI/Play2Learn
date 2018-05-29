from wtforms import Form
from wtforms import StringField, TextField, PasswordField, IntegerField, SelectMultipleField
from wtforms.fields.html5 import EmailField
from wtforms import validators

class CommentForm(Form):
	userID = StringField('ID de Usuario', 
		[
		validators.Required(),
		validators.length(min=8, max=10, message='Ingrese un ID válido (entre 8 y 10 caracteres)')
		]
		)
	username = StringField('Usuario', 
		[
		validators.Required(),
		validators.length(min=4, max=15, message='Ingrese un nombre de usuario válido (min 4 caracteres)')
		]
		)
	email = EmailField('Correo',
		[
		validators.Required(),
		validators.Email(message = 'Ingrese un email válido')
		]
		)
	password = PasswordField('Contraseña', 
		[
		validators.Required(),
		validators.length(min=4, max=20, message='Ingrese una contraseña válida (entre 4 y 20 caracteres)')
		]
		)
	grade = SelectMultipleField('Grado', choices=[('kinder','kinder'),('primero','primero'),('segundo','segundo'),('tercero','tercero'),('cuarto','cuarto'),
		('quinto','quinto'),('sexto','sexto'),('septimo','septimo'),('octavo','octavo'),('noveno','noveno'),('decimo','decimo'),('once','once')], validators=[validators.Required()])
		
		

