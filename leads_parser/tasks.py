import base64
from io import BytesIO

import pandas as pd
from celery import shared_task

from .parser import read_csv


@shared_task
def extract_csv_data(csv_file):
    csv_file = base64.b64decode(csv_file)
    bo = BytesIO(csv_file)
    dataframe = pd.read_csv(bo)
    sheet_id = read_csv(dataframe)
    return sheet_id
