from flask import Flask, render_template
import requests
import random
import json

app = Flask(__name__)


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/tracks/<genre>')
def get_tracks(genre):
    artist = get_artist_from_json_file(genre)
    return artist


def get_artist_from_json_file(genre):
    try:
        with open("genres.json", "r") as f:
            data = json.load(f)
        genre_values = data[genre.lower()]
        artist = genre_values[random.randint(0, len(genre_values) - 1)]

    except Exception:
        return None

    return artist


if __name__ == '__main__':
    app.run(debug=True)
