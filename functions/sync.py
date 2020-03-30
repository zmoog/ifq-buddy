import json
from datetime import date

from app.downloader import IFQDownloader
from app.uploader import OwncloudUploader

downloader = IFQDownloader()
uploader = OwncloudUploader()

def handle(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # download today IFQ
    local_path = downloader.download(date.today())

    # upload to owncloud
    uploader.upload(local_path, date.today())

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
