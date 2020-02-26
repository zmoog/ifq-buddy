import json

from datetime import date

from app.settings import IFQ_USERNAME, IFQ_PASSWORD
from app.sync import SyncTask
from ifq import Scraper

scraper = Scraper(IFQ_USERNAME, IFQ_PASSWORD)
task = SyncTask(scraper)


def handle(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # run the scheduled task
    task.run(date.today())

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
