import os
import json
from pprint import pprint
from flask import Flask, render_template, jsonify, send_from_directory, abort
from sq_db import get_all_locations_data, get_place_details, get_location_data, get_map_data

app = Flask(__name__)

IMAGE_DIRECTORY = os.path.join(app.root_path, 'static/images')


@app.route('/test')
def index():
    return jsonify("server is live"), 200


@app.route('/')
def main():
    return render_template('index.html'), 200


@app.route('/get_all_locations')
def get_all_locations():
    # print(get_all_locations_data(output_format='json'))
    return get_all_locations_data(output_format='json'), 200


@app.route('/get_img/<img_name>')
def get_image(img_name):
    try:
        return send_from_directory(IMAGE_DIRECTORY, img_name), 200
    except FileNotFoundError:
        abort(404)


@app.route('/place/<int:place_id>')
def place_detail(place_id):
    place_data = get_location_data(place_id, output_format='dict')
    place_details = get_place_details(place_id, output_format='dict')
    place_map = get_map_data(place_id, output_format='dict')

    final_data = place_data.copy()
    for key, value in place_details.items():
        final_data[key] = value

    for key, value in place_map.items():
        final_data[key] = value

    return render_template('place_detail.html', place=final_data), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
