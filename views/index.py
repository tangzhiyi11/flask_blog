from flask import render_template
from . import main


@main.route('/')
def get_index():
    return render_template('index.html')