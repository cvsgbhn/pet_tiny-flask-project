import os

import flask
from flask import Flask, request, jsonify, render_template
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(arg):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


def take_home_memes(universe):
    memes = os.listdir("./static/images/witcher")
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
    if request.method == 'POST':
        if request.form['universe_button'] == 'witcher':
            path = "./static/images/witcher"
            memes = os.listdir(path)
        if request.form['universe button'] == 'DC':
            path = "./static/images/dc"
            memes = os.listdir(path)
    else:
        #TODO: add collecting pics from all images/* folders
        path = "./static/images/witcher"
        memes = os.listdir("./static/images/witcher")
    mem = random.choice(memes)
    mem = path + '/' + mem
    universe_name = mem.split("/")[3]
    return render_template('home.html', mem=mem, universe_name=universe_name)


app.run()
