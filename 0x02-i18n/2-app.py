#!/usr/bin/env python3
"""
    This Module contains a basic set up of a flask_babel
"""
from flask_babel import Babel
from flask import Flask, render_template, request

app = Flask(__name__)


class Config:
    """
        This class is used to configure the Flask instance `app`
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
        This method is used to select the best choice of language
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """
        This is the home page
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
