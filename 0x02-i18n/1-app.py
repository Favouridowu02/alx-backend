#!/usr/bin/env python3
"""
    This Module contains the Flask app and a  single route
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """This Class is used to set up the Flask Babel Co  nfiguration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def home():
    """ This is the home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
