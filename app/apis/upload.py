from flask import Blueprint, request
from app.services.upload import UploadService
from app.helpers.errors import UBadRequest

upload_api = Blueprint("upload_api", __name__)


@upload_api.route("/image", methods=["POST"])
def upload():
    upload_service = UploadService()
    file = request.files["file"]
    if file.filename == "":
        raise UBadRequest("No filename")
        return
    if True:
        output = upload_service.upload_cloud(file, upload_service.S3_BUCKET)
        print("Image saved")
        return {"data": str(output)}
    else:
        raise UBadRequest("That file extension is not allowed")
