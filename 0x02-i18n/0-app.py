#!/usr/bin/env python3
"""
    This Module contains the Flask app and a  single route
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=True)
def home():
    """
        This is the Home page route
    """
    return render_template('0-index.html')
