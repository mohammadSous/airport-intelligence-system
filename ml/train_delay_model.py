from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
from utils.db_connection import get_engine

MODELS_DIR = Path(__file__).parent / "models"
SQL_ML_DIR = Path("sql/ml")


def load_ml_query(file_name):
    engine = get_engine()

    query_path = SQL_ML_DIR / file_name
    query = query_path.read_text()

    df = pd.read_sql(query, engine)
    return df


# Load ML dataset
df = load_ml_query("delay_dataset.sql")

# Separate features and target
X = df.drop("is_delayed", axis=1)
y = df["is_delayed"]

categorical_columns = [
    "airline",
    "origin",
    "destination",
    "gate_id"
]

numerical_columns = [
    "departure_hour",
    "departure_day_of_week",
    "tickets_sold",
    "average_ticket_price",
    "employee_count",
    "baggage_count",
    "total_baggage_weight"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns),
        ("num", StandardScaler(), numerical_columns)
    ]
)

X_processed = preprocessor.fit_transform(X)


#splitting the data 80/20
X_train, X_test, y_train, y_test = train_test_split(
    X_processed,
    y,
    test_size=0.2,
    random_state=42
)


#training
model = LogisticRegression(
    max_iter=1000,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)


#y_pred = model.predict(X_test)

#Save trained model + preprocessor using joblib
joblib.dump(model, MODELS_DIR / "delay_model.pkl")
joblib.dump(preprocessor, MODELS_DIR / "delay_preprocessor.pkl")