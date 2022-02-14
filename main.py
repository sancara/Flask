from django.shortcuts import redirect
from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

todos = ['Lau', 'San', 'Cata', 'Simi', '???']

@app.errorhandler
def not_found(error):
    return render_template('404.html', error=error)

@app.route('/')
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)

    return response

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    #crea un diccionario con todas las variables
    context = {
        'user_ip': user_ip,
        'todos': todos
    }
    #al pasar el **kwarg es como pasar las variables 1 por 1
    #pudiendo acceder a ellas directamente,
    #si pasaramos sólo context, deberíamos acceder a las variables
    #como context.user_ip
    return render_template('hello.html', **context)

