from flask import render_template

from . import bp 

@bp.route('/')
def home():
    matrix={
        'cars': ['Ford Mustang', 'Chevrolet Corvette', 'Audi R8', 'Porsche-911'],
        'drivers':['Jeff Gordon', 'Alain Prost', 'Jimmie Johnson', 'Richard Petty', 'Nigel Mansell', 'Michael Schumacher']
    }
    return render_template('index.jinja', title='Home', cars=matrix['cars'], drivers=matrix['drivers'])


@bp.route('/about')
def about():
    return render_template('about.jinja')
