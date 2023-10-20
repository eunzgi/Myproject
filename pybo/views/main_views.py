from flask import Blueprint, url_for, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


# @bp.route('/')
# def index():
#     return redirect(url_for('question._list'))

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/enoughus')
def enoughus():
    return render_template('enoughus.html')

@bp.route('/sub01')
def sub01():
    return render_template('sub01.html')

@bp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')