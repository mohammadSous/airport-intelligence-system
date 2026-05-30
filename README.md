# Airport Intelligence System

## Overview

Airport Intelligence System is an end-to-end data analytics project built using MySQL, Python, Pandas, Streamlit, and FastAPI.

The project simulates an airport management environment and demonstrates the complete workflow of:

* Database design
* Data generation and storage
* SQL analytics and reporting
* Python data processing
* Data visualization
* Interactive dashboard development
* REST API development
* Future machine learning integration

The goal of this project is to strengthen practical data science, data engineering, machine learning, and software development skills through a realistic end-to-end application.

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

### Development Tools

* Git
* GitHub
* VS Code

---

## Project Structure

```text
airport-intelligence-system/

├── api/
│   ├── main.py
│   └── routes/
│
├── dashboard/
│   ├── app.py
│   └── pages/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── exports/
│
├── ml/
│   ├── train_model.py
│   ├── predict.py
│   ├── preprocessing.py
│   ├── evaluate_model.py
│   └── models/
│
├── notebooks/
│
├── screenshots/
│
├── sql/
│   ├── schema.SQL
│   ├── inserts.SQL
│   ├── queries.SQL
│   └── reports/
│
├── utils/
│   ├── db_connection.py
│   ├── load_queries.py
│   └── helpers.py
│
├── tests/
│
├── analysis.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Database Design

The project includes a custom relational database that models airport operations.

Main entities include:

* Airports
* Airlines
* Flights
* Passengers
* Tickets
* Baggage
* Employees
* Employee Assignments

The database was designed using SQL and populated with synthetic data for analysis and reporting purposes.

---

## SQL Analytics Reports

The project currently includes the following analytical reports:

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
* Execute SQL reports
* Load results into Pandas DataFrames
* Generate visualizations with Matplotlib
* Reuse functionality through helper modules

Reusable utilities include:

* Database connection management
* SQL report loading
* Shared configuration dictionaries
* Centralized report definitions

---

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard for exploring airport analytics reports.

Current dashboard features:

* Summary metrics
* Total flights overview
* Delayed flights overview
* Revenue overview
* Static delayed flights visualization
* Sidebar report selection
* Interactive report exploration
* Dynamic report tables
* Dynamic visualizations

### Run the Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## FastAPI Backend

The project includes a FastAPI backend that exposes airport analytics reports through REST API endpoints.

The API retrieves data from the MySQL database, executes SQL reports through reusable Python utilities, and returns the results as JSON.

### Features

* Report endpoints
* Summary metrics endpoint
* JSON responses
* Automatic interactive API documentation
* Reusable integration with existing SQL reports

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
* JSON APIs
* Python package structure
* Modular project organization
* Git and GitHub workflows

---

## Future Development

### Machine Learning Module

Planned machine learning functionality includes:

* Feature engineering
* Data preprocessing
* Train/test splitting
* Delay prediction model
* Model evaluation
* Model persistence
* Prediction API integration

### Dashboard Improvements

* Additional visualizations
* Advanced filtering
* Multi-page dashboard expansion

### Backend Improvements

* Additional API endpoints
* Request validation
* Error handling improvements

### Project Improvements

* Automated testing
* Documentation improvements
* Deployment preparation

---

## Author

Mohammad Sous

AI & Data Science Student

Al-Zaytoonah University of Jordan
