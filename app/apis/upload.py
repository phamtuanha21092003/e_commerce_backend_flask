from flask import Blueprint, request
from app.services.upload import UploadService
from app.helpers.errors import UBadRequest
import hashlib
import datetime

upload_api = Blueprint("upload_api", __name__)

upload_service = UploadService()


@upload_api.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    if file.filename == "":
        raise UBadRequest("No filename")
    suffix = _create_suffix(file)
    output = upload_service.upload_cloud(file, suffix)
    return {"data": str(output)}


def _create_suffix(file):
    hash_file = hashlib.md5(
        "{}{}".format(file.read(), datetime.datetime.now()).encode("utf-8")
    ).hexdigest()
    file.seek(0)
    return "files/{}/".format(hash_file)
