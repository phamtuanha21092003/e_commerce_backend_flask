import os
import boto3
from app.helpers.errors import UBadRequest
import re


class UploadService:
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG", "GIF", "WEBP", "JP2"]
    S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
    S3_KEY = os.getenv("S3_KEY")
    S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")
    S3_BUCKET = os.getenv("S3_BUCKET")
    CDN = "http://localhost:9000/{}/".format(S3_BUCKET)

    def upload_cloud(self, file, suffix="files"):
        if file.filename == "":
            raise UBadRequest("No filename")
        if self.allowed_image(file.filename):
            output = self.upload_file_to_s3(
                file, UploadService.S3_BUCKET, suffix=suffix
            )
            print("Image saved")
            return str(output)
        else:
            raise UBadRequest("That file extension is not allowed")


    def allowed_image(self, filename):
        if not ("." in filename):
            return False

        ext = filename.rsplit(".", 1)[1]

        if ext.upper() in UploadService.ALLOWED_IMAGE_EXTENSIONS:
            return True
        else:
            return False


    def upload_file_to_s3(
            self, file, bucket_name, acl="public-read", suffix="files/"
    ):
        s3 = boto3.client(
            service_name='s3',
            endpoint_url=UploadService.S3_ENDPOINT_URL,
            aws_access_key_id=UploadService.S3_KEY,
            aws_secret_access_key=UploadService.S3_SECRET
        )
        s3_resource = boto3.resource(
            service_name='s3',
            endpoint_url=UploadService.S3_ENDPOINT_URL,
            aws_access_key_id=UploadService.S3_KEY,
            aws_secret_access_key=UploadService.S3_SECRET
        )
        file_name = re.sub(r"[^a-zA-Z0-9._-]+", '', file.filename)
        try:
            bucket = s3_resource.Bucket(bucket_name)
            list_file = list(bucket.objects.filter(Prefix=suffix))
            if list_file:
                file_name = list_file[0].key.split('/')[-1]
                is_resize = False
                if ("." in file_name):
                    for s3_file in list_file:
                        split_l = s3_file.key.split('/')[-1]
                        if not ("." in split_l):
                            continue
                        split_l = split_l.rsplit(".", 1)[0]
                        split_i = file_name.rsplit(".", 1)[0]
                        if split_l == '{}_96'.format(split_i):
                            is_resize = True
                if not is_resize:
                    print("Re optimize image")
                return "{}{}".format(UploadService.CDN, list_file[0].key)

            s3.upload_fileobj(
                file,
                bucket_name,
                '{}{}'.format(suffix, file_name),
                ExtraArgs={
                    "ACL": acl,
                    "ContentType": file.content_type,
                    "CacheControl": "max-age=31536000",
                }
            )

        except Exception as e:
            print("Something Happened: ", e)
            raise e
        return "{}{}{}".format(UploadService.CDN, suffix, file_name)
