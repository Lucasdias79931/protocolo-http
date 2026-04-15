from flask import Blueprint, request, jsonify, send_file
from http import HTTPStatus

from ..services import FileService

file_route = Blueprint('file', __name__)


@file_route.route('/image', methods=['POST'])
def upload_image():

    if 'file' not in request.files:
        return jsonify({
            "error": "file is required"
        }), HTTPStatus.BAD_REQUEST

    file = request.files['file']

    if file.filename == '':
        return jsonify({
            "error": "filename is empty"
        }), HTTPStatus.BAD_REQUEST

    filename, id_file = FileService.save_file(file)

    return jsonify({
        "message": "file uploaded successfully",
        "filename": filename,
        "id_file": id_file
    }), HTTPStatus.CREATED


@file_route.route('/image', methods=['GET'])
def get_image():

    image_id = request.args.get('image_id')
    filename = request.args.get('filename')

    if not image_id or not filename:
        return jsonify({
            'message': "image_id and filename must be sent"
        }), HTTPStatus.BAD_REQUEST

    path = FileService.get_file_path(filename, image_id)

    if path is None:
        return jsonify({
            "error": "file not found"
        }), HTTPStatus.NOT_FOUND

    return send_file(path), HTTPStatus.OK


@file_route.route('/list-images-path', methods=['GET'])
def get_list_path():

    images = FileService.list_images()

    if not images:
        return jsonify({
            "message": "no images found",
            "data": []
        }), HTTPStatus.OK

    return jsonify({
        "data": images
    }), HTTPStatus.OK