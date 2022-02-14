from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)

todos = ['Lau', 'San', 'Cata', 'Simi', '???']

app.config['SECRET_KEY'] = 'ASDFñlkj!23'

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Enviar')

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

@app.route('/hello')
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    #crea un diccionario con todas las variables
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login': login_form
    }
    #al pasar el **kwarg es como pasar las variables 1 por 1
    #pudiendo acceder a ellas directamente,
    #si pasaramos sólo context, deberíamos acceder a las variables
    #como context.user_ip
    return render_template('hello.html', **context)

