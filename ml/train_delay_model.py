from pathlib import Path
import pandas as pd

from utils.db_connection import get_engine

SQL_ML_DIR = Path("sql/ml")

ML_QUERY = {
    "Delay Dataset": "delay_dataset.sql"
}

def load_ml_query(query_name):
    engine = get_engine()

    file_name = ML_QUERY[query_name]
    query_path = SQL_ML_DIR / file_name
    query = query_path.read_text()

    df = pd.read_sql(query, engine)
    return df


for query_name in ML_QUERY:
    df = load_ml_query(query_name)

    print("\n" + "=" * 60)
    print(query_name)
    print("=" * 60)
    print(df.head(10))


X = df.drop("is_delayed", axis=1)
y = df["is_delayed"]

print(X.dtypes)
