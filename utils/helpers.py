import json
def dataframe_to_records(df):
    """
    Convert a Pandas DataFrame into JSON-friendly records.
    """
    return json.loads(
        df.to_json(
            orient="records",
            date_format="iso"
        )
    )   