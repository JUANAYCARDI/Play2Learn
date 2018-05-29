from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import *
from Database import *

import loginform
import registerform

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
	comment_form = loginform.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		usuario = comment_form.username.data
		contraseña = comment_form.password.data
		if checkData(usuario,contraseña) == True:
			return redirect(url_for('admin'))
		elif checkData(usuario,contraseña) == False: 
			grado = checkGrade(usuario)
			userID = checkUserID(usuario)
			lifes = checkLife(userID)
			Cquestions = checkCquestions(userID)
			Iquestions = checkIquestions(userID)
			if grado == 'kinder ':
				return redirect(url_for('kinder'))
			elif grado == 'primero ':
				return redirect(url_for('primero'))
			elif grado == 'segundo ':
				return redirect(url_for('segundo'))
			elif grado == 'tercero ':
				return redirect(url_for('tercero'))
			elif grado == 'cuarto ':
				return redirect(url_for('cuarto'))
			elif grado == 'quinto ':
				return redirect(url_for('quinto'))
			elif grado == 'sexto ':
				return redirect(url_for('sexto'))
			elif grado == 'septimo ':
				return redirect(url_for('septimo'))
			elif grado == 'octavo ':
				return redirect(url_for('octavo'))
			elif grado == 'noveno ':
				return redirect(url_for('noveno'))
			elif grado == 'decimo ':
				return redirect(url_for('decimo'))
			elif grado == 'once ':
				return redirect(url_for('once'))
		elif checkData(usuario,contraseña) == 'wrong':
			return render_template('login.html', form = comment_form, contraseña = 'incorrecta')
		elif checkData(usuario,contraseña) == None:
			print(None)
			return render_template('login.html', form = comment_form, user = 'incorrecto')
	return render_template('login.html', form = comment_form, contraseña = '', user = '' )
	
@app.route('/admin', methods = ['GET','POST'])
def admin():
	
	return render_template('admin.html')

@app.route('/kinder', methods = ['GET', 'POST'])
def kinder():
	grado = 'kinder'
	return render_template('game1.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/kinder1Q', methods = ['GET', 'POST'])
def kinder1Q():
	grado = 'kinder'
	return render_template('game1Q.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)	

@app.route('/kinder2Q', methods = ['GET', 'POST'])
def kinder2Q():
	grado = 'kinder'
	return render_template('game2Q.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)	

@app.route('/kinder3Q', methods = ['GET', 'POST'])
def kinder3Q():
	grado = 'kinder'
	return render_template('game3Q.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)	

@app.route('/kinder4Q', methods = ['GET', 'POST'])
def kinder4Q():
	grado = 'kinder'
	return render_template('game4Q.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)	

@app.route('/primero', methods = ['GET', 'POST'])
def primero():
	grado = 'primero'
	return render_template('game2.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/segundo', methods = ['GET', 'POST'])
def segundo():
	grado = 'segundo'
	return render_template('game2.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/tercero', methods = ['GET', 'POST'])
def tercero():
	grado = 'tercero'
	return render_template('game2.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/cuarto', methods = ['GET', 'POST'])
def cuarto():
	grado = 'cuarto'
	return render_template('game2.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/quinto', methods = ['GET', 'POST'])
def quinto():
	grado = 'quinto'
	return render_template('game2.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/sexto', methods = ['GET', 'POST'])
def sexto():
	grado = 'sexto'
	return render_template('game3.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/septimo', methods = ['GET', 'POST'])
def septimo():
	grado = 'septimo'
	return render_template('game3.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/octavo', methods = ['GET', 'POST'])
def octavo():
	grado = 'octavo'
	return render_template('game3.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/noveno', methods = ['GET', 'POST'])
def noveno():
	grado = 'noveno'
	return render_template('game3.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/decimo', methods = ['GET', 'POST'])
def decimo():
	grado = 'decimo'
	return render_template('game4.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/once', methods = ['GET', 'POST'])
def once():
	grado = 'once'
	return render_template('game4.html', grado = grado, lifes = 5, Cquestions = 0, Iquestions = 0)

@app.route('/graduacion', methods = ['GET', 'POST'])
def graduacion():
	return render_template('endgame.html')

	
@app.route('/admin/register', methods = ['GET', 'POST'])
def register():
	comment_form = registerform.CommentForm(request.form)
	if request.method == 'POST' and comment_form.validate():
		userID = comment_form.userID.data
		usuario = comment_form.username.data
		correo = comment_form.email.data
		contraseña = comment_form.password.data
		grado = comment_form.grade.data
		str1 = " ".join(str(x) for x in grado)
		grado = str1
		state = addUser(userID, usuario, correo, contraseña, grado)
		
		if state == 'Done':
			return render_template('register.html', form = comment_form, UserID = 'N', User = 'N', Mail = 'N')

		elif state == 'UserIDE':
			return render_template('register.html', form = comment_form, UserID = 'E', User = 'N', Mail = 'N')

		elif state == 'UserE':
			return render_template('register.html', form = comment_form, UserID = 'N', User = 'E', Mail = 'N')

		elif state == 'MailE':
			return render_template('register.html', form = comment_form, UserID = 'N', User = 'N', Mail = 'E')

	return render_template('register.html', form = comment_form)

if __name__ == '__main__':
	app.run(debug=True)