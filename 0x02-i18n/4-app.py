#!/usr/bin/env python3
"""4. Force locale with URL parameter
"""
from flask import Flask
from flask import render_template
from flask import request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


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


@app.route("/", strict_slashes=False)
def hello_world() -> str:
    """Hello Holberton
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
