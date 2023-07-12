from flask import Flask, render_template, make_response, jsonify, request, redirect
from http import cookies
import requests
import random
import json
import datetime

app = Flask(__name__)

cookie_key = "access_key"


@app.route('/home')
@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie(cookie_key, get_access_token_from_service(), max_age=3600)
    return resp


@app.route('/tracks/<genre>', methods=['GET'])
def get_tracks(genre):
    artist = get_artist_from_json_file(genre)

    if artist is None:
        return []

    access_token = get_access_token_from_cookie()

    api_result = get_tracks_values(access_token, artist)

    result = set_response_dto(api_result)

    return jsonify(result)


def set_response_dto(api_result):
    result = []
    for item in api_result['tracks']['items']:
        track_info = {
            "artist": item['artists'][0]['name'],
            "track": item['name'],
            "album_image_url": item['album']['images'][0]['url'],
            "preview_url": item['preview_url']
        }
        result.append(track_info)

    return result


def get_tracks_values(access_token, artist):
    url = 'https://api.spotify.com/v1/search'

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    params = {
        'q': f'artist:"{artist}"',
        'type': 'track',
        'limit': 10,
        'sort': 'popularity'
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        tracks = response.json()
        return tracks
    else:
        return []


def get_access_token_from_cookie():
    cookie_value = request.cookies.get(cookie_key)
    if cookie_value is None:
        cookie_value = get_access_token_from_service()
    return cookie_value


def get_access_token_from_service():
    if request.cookies.get(cookie_key) is not None:
        return request.cookies.get(cookie_key)

    credential_data = get_credential_data_from_json_file()
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, headers=headers, data=credential_data)

    access_token = response.json()['access_token']

    return access_token


def get_credential_data_from_json_file():
    with open("credential.json", "r") as f:
        data = json.load(f)
    return data


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
