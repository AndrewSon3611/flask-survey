from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickensarecool1234"

debug = DebugToolbarExtension(app)