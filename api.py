import os

import flask
from flask import Flask, request, jsonify, render_template
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.errorhandler(404)
def page_not_found():
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


def take_home_memes():
    memes = os.listdir("./static/")
    return memes


def shut_up_and_shuffle(array):
    shuffled_array = []
    i = 0
    while i < len(array):
        current_selection = random.choice(array)
        if current_selection not in shuffled_array:
            shuffled_array.append(current_selection)
        i = i+1
    return shuffled_array


@app.route('/')
def show_picture():
    memes = take_home_memes()
    mem = random.choice(memes)
    mem = './static/images' + mem
    return render_template('home.html', mem=mem)


app.run()
