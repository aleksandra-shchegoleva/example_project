from flask import render_template
from app import app
from app.login import LoginForm

@app.route('/')
def start():
  form = LoginForm()
  return render_template('index.html', form=form)