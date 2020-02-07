from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nok'}
    posts = [
        {
            'author': {'username': 'Roan'},
            'body': 'Matulog ka na babe'
        },
        {
            'author': {'username': 'Noki'},
            'body': 'Ayoko nga'
        }
    ]
    return render_template('index.html', title='Home', user=user. posts=posts)
