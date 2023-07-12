from flask import Flask, render_template
import requests
import random
import json
import datetime

app = Flask(__name__)

expires = datetime.datetime.now()
access_key = ""


@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/tracks/<genre>')
def get_tracks(genre):
    artist = get_artist_from_json_file(genre)

    if artist is None:
        return []

    return artist


def get_access_key():
    if datetime.datetime.now() < expires and access_key is not None and len(access_key) != 0:
        return access_key
    else:
        return ""
    return ""


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
