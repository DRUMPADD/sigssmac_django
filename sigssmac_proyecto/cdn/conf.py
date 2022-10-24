import os

AWS_ACCESS_KEY_ID=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME="sigssmac"
AWS_S3_ENDPOINT_URL="https://nyc3.digitaloceanspaces.com"

AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=84600",
}
AWS_LOCATION="https://sigssmac.nyc3.digitaloceanspaces.com"

DEFAULT_FILE_STORAGE="sigssmac_proyecto.cdn.backends.MediaRootS3Boto3Storage"
STATICFILES_STORAGE="sigssmac_proyecto.cdn.backends.StaticRootS3Boto3Storage"