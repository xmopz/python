from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/page')
def page():
    return render_template('page.html')