import pandas as pd
from .models import Customer, Sheet
from .validators import is_number_in_international_format
from io import BytesIO


def read_csv(dataframe):
    column_names = list(dataframe.columns)
    sheet = Sheet()
    sheet.save()
    for index, row in dataframe.iterrows():
        # if not is_number_in_international_format(row["Mobile"]):
        #     continue
        if pd.isnull(row["Name"]):
            continue
        if pd.isnull(row["Mobile"]):
            continue
        if pd.isnull(row["Status"]):
            continue
        customer = Customer(
            name=row["Name"],
            mobile=row["Mobile"],
            status=row["Status"],
            address=row["Address"],
            industry=row["Industry"],
            website=row["Website"],
            contacts=row["Contacts"],
            pipelines=row["Pipelines"],
            notes=row["Notes"],
            sheet_id=sheet
        )
        customer.save()
    return sheet.id
