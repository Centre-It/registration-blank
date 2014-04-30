# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
from forms import *
from core import main

app = Flask(__name__)

app.config['RECAPTCHA_PUBLIC_KEY'] = '6LeYIbsSAAAAACRPIllxA7wvXjIE411PfdB2gt2J'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LeYIbsSAAAAAJezaIq3Ft_hSTo0YtyeFG-JgRtu'


@app.route('/')
def index():
    return redirect('/signup')


@app.route('/signup', methods=('GET', 'POST'))
def singup():
    form = SignUpForm(csrf_enabled=False)

    if form.validate_on_submit():
        if not main.process_data(form.data):
            return redirect('/error')

        return redirect('/success')

    return render_template('signup.html', form=form)


@app.route('/success')
def success():
    return "Ваша заявка принята"


@app.route('/error')
def error():
    return "Произошла внутренняя ошибка. Попробуйте позже"

if __name__ == '__main__':
    app.run(host='172.16.7.32', port=5000)
