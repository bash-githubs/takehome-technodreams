from .parser import read_csv
import base64
from celery import shared_task
import pandas as pd
from io import BytesIO


@shared_task
def extract_csv_data(csv_file):
    csv_file = base64.b64decode(csv_file)
    bo = BytesIO(csv_file)
    dataframe = pd.read_csv(bo)
    sheet_id = read_csv(dataframe)
    return sheet_id
