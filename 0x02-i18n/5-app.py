#!/usr/bin/env python3
"""5. Mock logging in
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel
from typing import Dict


app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class for Flask
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[Dict, None]:
    """ function that returns a user dictionary
    or None if the ID cannot be found or if login_as
    was not passed.
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    user = get_user()
    g.user = user


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """Hello Holberton
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
