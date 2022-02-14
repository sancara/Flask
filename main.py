from flask import Flask, request, make_response, redirect, \
    render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Lau', 'San', 'Cata', 'Simi', '???']

app.config['SECRET_KEY'] = 'ASDFñlkj!23'

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    test = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(test)
    

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
   
    #crea un diccionario con todas las variables
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login1': login_form,
        'username': username
    }
    #al pasar el **kwarg es como pasar las variables 1 por 1
    #pudiendo acceder a ellas directamente,
    #si pasaramos sólo context, deberíamos acceder a las variables
    #como context.user_ip

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        password = login_form.password.data
        session['password'] = password

        flash('Nombre de usuario registrado con éxito!')

        return redirect(url_for('index'))
    
    return render_template('hello.html', **context)

