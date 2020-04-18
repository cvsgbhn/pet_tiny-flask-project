import os

import flask
from flask import Flask, request, jsonify, render_template
import random

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.errorhandler(404)
def page_not_found(arg):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

def shut_up_and_shuffle(array):
    shuffled_array = []
    i = 0
    while i < len(array):
        current_selection = random.choice(array)
        if current_selection not in shuffled_array:
            shuffled_array.append(current_selection)
        i = i+1
    return shuffled_array

@app.route('/getimage')
def get_img():
    universe = request.args['universe'];
    print(universe)
    memes = os.listdir("./static/images/{}".format(universe))
    return random.choice(memes)

@app.route('/')
@app.route('/witcher')
def get_witcher_picture():
    #TODO: add collecting pics from all images/* folders
    path = "./static/images/witcher"
    memes = os.listdir("./static/images/witcher")
    mem = random.choice(memes)
    mem = path + '/' + mem
    universe_name = mem.split("/")[3]
    return render_template('home.html', mem=mem, title=universe_name)

@app.route('/dc')
def get_dc_picture():
    #TODO: add collecting pics from all images/* folders
    path = "./static/images/dc"
    memes = os.listdir("./static/images/dc")
    mem = random.choice(memes)
    mem = path + '/' + mem
    universe_name = mem.split("/")[3]
    return render_template('home.html', mem=mem, title=universe_name)

@app.route('/to_universe')
def get_universe_route():
    return redirect(url_for('/dc'))

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
