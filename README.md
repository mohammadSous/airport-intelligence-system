# Airport Intelligence System

## Overview

Airport Intelligence System is an end-to-end data analytics and machine learning project built using MySQL, Python, Pandas, Streamlit, FastAPI, and Scikit-Learn.

The project simulates airport operations and demonstrates a complete data workflow, starting from relational database design and SQL analytics, then extending into dashboard development, REST API integration, and machine learning-based flight delay prediction.

The system includes:

* Relational database design and synthetic data generation
* Analytical SQL reporting
* Python-based data processing and visualization
* Interactive Streamlit dashboard
* FastAPI backend with REST endpoints
* Flight delay prediction using machine learning
* Model deployment through an API and dashboard interface

The goal of this project is to develop practical experience in data analytics, machine learning workflows, backend development, and data-driven application design through a realistic airport operations use case.

---

## Key Features

* Custom MySQL airport operations database
* Synthetic operational data for flights, passengers, baggage, tickets, employees, and gates
* 10 reusable analytical SQL reports
* Python analytics layer using Pandas and SQLAlchemy
* Data visualizations using Matplotlib and Streamlit
* Interactive Streamlit dashboard
* FastAPI backend with JSON endpoints
* Flight delay prediction using Scikit-Learn
* Machine learning preprocessing pipeline using ColumnTransformer
* Saved trained model and preprocessor
* Prediction API endpoint
* Dashboard prediction form with delay probability output

---

## Technologies Used

### Database

* MySQL

### Python Libraries

* Pandas
* NumPy
* SQLAlchemy
* PyMySQL
* Matplotlib
* Streamlit
* FastAPI
* Uvicorn
* Scikit-Learn
* Joblib
* Requests

### Development Tools

* Git
* GitHub
* VS Code

---

## Project Structure
'''
airport-intelligence-system/

├── api/
│   ├── main.py
│   ├── __init__.py
│   └── routes/
│       ├── airlines.py
│       ├── flights.py
│       ├── predictions.py
│       ├── reports.py
│       ├── summary.py
│       └── __init__.py
│
├── dashboard/
│   ├── app.py
│   └── __init__.py
│
├── ml/
│   ├── predict.py
│   ├── train_delay_model.py
│   ├── __init__.py
│   └── models/
│       ├── delay_model.pkl
│       └── delay_preprocessor.pkl
│
├── screenshots/
│   ├── dashboard/
│   │   └── dashboard_overview.png
│   └── graphs/
│       ├── avg_baggage_weight_by_type.png
│       ├── employee_flight_assignment_count.png
│       ├── flights_by_status.png
│       ├── flights_per_airline.png
│       ├── most_popular_destinations.png
│       └── total_revenue_per_airline.png
│
├── sql/
│   ├── schema.SQL
│   ├── inserts.SQL
│   ├── queries.SQL
│   ├── ml/
│   │   └── delay_dataset.sql
│   └── reports/
│       ├── average_baggage_weight_by_type.sql
│       ├── average_ticket_price_per_airline.sql
│       ├── baggage_count_per_passenger.sql
│       ├── delayed_flights_per_airline.sql
│       ├── employee_flight_assignment_count.sql
│       ├── flights_by_status.sql
│       ├── flights_per_airline.sql
│       ├── most_popular_destinations.sql
│       ├── tickets_sold_per_flight.sql
│       └── total_revenue_per_airline.sql
│
├── utils/
│   ├── db_connection.py
│   ├── helpers.py
│   ├── load_queries.py
│   └── __init__.py
│
├── check_reports.py
├── visualizations.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Database Design

The project includes a custom relational database that models airport operations.

Main entities include:

* Airports
* Flights
* Passengers
* Tickets
* Baggage
* Employees
* Employee Assignments
* Gates

The database was designed using SQL and populated with synthetic operational data for analysis, reporting, dashboard exploration, API responses, and machine learning feature engineering.

The schema supports relationships such as:

* Flights connected to airports and gates
* Tickets connected to passengers and flights
* Baggage connected to passengers
* Employees assigned to flights
* Employee phone records stored separately

---

## SQL Analytics Reports

The project includes 10 analytical SQL reports:

* Flights per Airline
* Delayed Flights per Airline
* Average Ticket Price per Airline
* Total Revenue per Airline
* Most Popular Destinations
* Tickets Sold per Flight
* Baggage Count per Passenger
* Average Baggage Weight by Type
* Employee Flight Assignment Count
* Flights by Status

All reports are stored as reusable SQL files and executed dynamically through Python.

---

## Python Analytics Layer

Python is used to:

* Connect to MySQL using SQLAlchemy
* Execute SQL report files
* Load SQL results into Pandas DataFrames
* Generate visualizations
* Reuse functionality through helper modules
* Convert DataFrames into JSON-friendly API responses

Reusable utilities include:

* Database connection management
* SQL report loading
* Shared report dictionaries
* JSON conversion helpers

---

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring airport analytics and using the machine learning delay prediction model.

### Dashboard Features

* Summary KPI metrics
* Total flights overview
* Delayed flights overview
* Revenue overview
* Static delayed flights visualization
* Sidebar report selection
* Interactive report exploration
* Dynamic report tables
* Dynamic visualizations
* Flight delay prediction form
* Real-time prediction result
* Delay probability display

### Run the Dashboard

```bash
python -m streamlit run dashboard/app.py
```

The FastAPI backend should also be running when using the prediction form.

---

## FastAPI Backend

The project includes a FastAPI backend that exposes airport analytics reports and machine learning predictions through REST API endpoints.

The API retrieves data from the MySQL database, executes SQL reports through reusable Python utilities, returns analytics results as JSON, and exposes a POST endpoint for flight delay prediction.

### Backend Features

* Report endpoints
* Flight report endpoints
* Airline report endpoints
* Summary metrics endpoint
* Flight delay prediction endpoint
* JSON responses
* Automatic interactive API documentation
* Reusable integration with SQL reports and ML model

### Run the API

```bash
python -m uvicorn api.main:app --reload
```

### API URLs

Homepage:

```text
http://127.0.0.1:8000
```

Interactive API Documentation:

```text
http://127.0.0.1:8000/docs
```

### Example Endpoints

List all available reports:

```text
GET /api/reports
```

Return a complete report:

```text
GET /api/reports/flights-per-airline
```

Return a report preview:

```text
GET /api/reports/flights-per-airline/preview?limit=5
```

Return dashboard summary metrics:

```text
GET /api/summary
```

Return flight-related reports:

```text
GET /api/flights
```

Return airline-related reports:

```text
GET /api/airlines
```

Predict flight delay:

```text
POST /api/predictions/delay
```

Example prediction request:

```json
{
  "airline": "Flynas",
  "origin": "Amman",
  "destination": "Cairo",
  "gate_id": "A0009",
  "departure_hour": 0,
  "departure_day_of_week": 2,
  "tickets_sold": 20,
  "average_ticket_price": 122.13,
  "employee_count": 4,
  "baggage_count": 30,
  "total_baggage_weight": 1735.92
}
```

Example prediction response:

```json
{
  "prediction": "Delayed",
  "delay_probability": 0.6987
}
```

---

## Machine Learning

The project includes a flight delay prediction system built using Scikit-Learn and integrated into both the FastAPI backend and Streamlit dashboard.

The objective is to predict whether a flight is likely to be delayed based on operational flight data.

### Machine Learning Workflow

* SQL-based feature engineering
* Flight-level dataset construction
* Data loading into Pandas
* Feature and target separation
* Categorical feature encoding using One-Hot Encoding
* Numerical feature scaling using StandardScaler
* Combined preprocessing using ColumnTransformer
* Train/Test split evaluation
* Logistic Regression classifier
* Balanced Logistic Regression classifier
* Random Forest classifier
* Tuned Random Forest classifier
* Confusion Matrix analysis
* Precision, Recall, and F1-score evaluation
* Model comparison and selection
* Model persistence using Joblib
* Prediction function using saved model and preprocessor
* FastAPI prediction endpoint
* Streamlit prediction interface

### Prediction Target

The classification target is:

```text
is_delayed
```

Where:

```text
0 = Not Delayed
1 = Delayed
```

### Prediction Features

The model uses operational flight features including:

* Airline
* Origin
* Destination
* Gate ID
* Departure Hour
* Departure Day of Week
* Tickets Sold
* Average Ticket Price
* Employee Count
* Baggage Count
* Total Baggage Weight

### Model Selection

Multiple models were evaluated for flight delay prediction.

Although Random Forest achieved higher overall accuracy, Balanced Logistic Regression was selected as the final model because it achieved significantly higher recall on delayed flights.

This decision was made because the business objective is not only to maximize overall accuracy, but to identify as many delayed flights as possible before departure.

### Final Selected Model

Balanced Logistic Regression

| Metric                             |       Result |
| ---------------------------------- | -----------: |
| Accuracy                           |        61.5% |
| Delay Recall                       |          66% |
| Delayed Flights Correctly Detected | 35 out of 53 |

### Why Recall Matters

For this use case, recall is important because missing an actual delayed flight is more costly than raising some false alarms.

A model with higher recall helps airport staff identify potential delays earlier, allowing for better planning, communication, and operational preparation.

---

## Screenshots

Screenshots are stored in the `screenshots/` folder.

Suggested screenshot categories:

```text
screenshots/
├── dashboard/
├── api/
├── ml/
└── graphs/
```

Examples include:

* Dashboard overview
* Report explorer
* Delay prediction form
* Prediction result
* Swagger API documentation
* Prediction endpoint test
* Generated visualizations

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone <repository-url>
cd airport-intelligence-system
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up the Database

Create the MySQL database and run:

```text
sql/schema.SQL
sql/inserts.SQL
```

The project assumes the local MySQL database is named:

```text
airport_intelligence
```

### 4. Run the API

```bash
python -m uvicorn api.main:app --reload
```

### 5. Run the Dashboard

```bash
python -m streamlit run dashboard/app.py
```

### 6. Train the ML Model

```bash
python -m ml.train_delay_model
```

This creates the saved model and preprocessor files inside:

```text
ml/models/
```

### 7. Test Prediction Logic

```bash
python -m ml.predict
```

---

## What I Learned

Through this project I practiced:

* Relational database design
* SQL querying and aggregation
* JOIN operations
* Data analysis with Pandas
* Database connectivity with SQLAlchemy
* Data visualization with Matplotlib
* Streamlit dashboard development
* FastAPI backend development
* REST API design
* GET and POST endpoints
* JSON APIs
* Pydantic request validation
* Python package structure
* Modular project organization
* Git and GitHub workflows
* Machine learning dataset construction
* Feature engineering using SQL
* Machine learning preprocessing
* One-Hot Encoding
* Feature scaling with StandardScaler
* ColumnTransformer pipelines
* Train/Test splitting
* Logistic Regression
* Random Forest
* Classification metrics
* Confusion Matrix analysis
* Precision, Recall, and F1-score evaluation
* Model comparison and selection
* Model persistence using Joblib
* Integrating ML predictions into APIs
* Connecting ML predictions to a dashboard interface

---

## Future Improvements

### Machine Learning Improvements

* Add aircraft operational data
* Add weather and airport congestion features
* Track delay reasons and delay duration
* Add aircraft maintenance and crew readiness data
* Experiment with additional classification models
* Tune probability thresholds for different business goals
* Improve model evaluation using cross-validation

### Dashboard Improvements

* Add advanced filtering
* Add more interactive visualizations
* Expand into a multi-page dashboard
* Add model explanation or feature importance views
* Improve prediction form usability

### Backend Improvements

* Add authentication and authorization
* Add more analytics endpoints
* Improve request validation
* Improve error handling
* Add automated API tests

### Deployment Improvements

* Add Docker support
* Deploy the API and dashboard
* Add environment variable configuration
* Add CI/CD workflow

---

## Author

Mohammad Sous