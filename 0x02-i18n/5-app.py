#!/usr/bin/env python3
"""
    This Module contains a basic set up of a flask_babel
"""
from flask_babel import Babel
from flask import Flask, render_template, request, g
from typing import Union, Dict

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """
        This Method is used to get the user
    """
    login_as = request.args.get('login_as')
    user = users.get(login_as, None)
    return user


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
def get_locale() -> str:
    """
        This method is used to select the best choice of language
    """
    locale = request.args.get('locale')
    locale = locale if locale in ['en', 'fr'] else 'en'
    return locale


@app.before_request
def before_request() -> None:
    """
        This method would be ran before any request is made
    """
    user = get_user()
    g.user = user


@app.route('/')
def home() -> str:
    """
        This is the home page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
