# Airport Intelligence System

## Overview

Airport Intelligence System is a data analytics project built using SQL, Python, Pandas, and Streamlit.

The project simulates an airport management environment and demonstrates the complete workflow of:

* Database design
* Data generation and storage
* SQL analytics and reporting
* Python data processing
* Data visualization
* Interactive dashboard development

The goal of this project is to strengthen practical data science, data engineering, and software development skills through a realistic end-to-end application.

---

## Technologies Used

### Database

* MySQL

### Python Libraries

* Pandas
* SQLAlchemy
* PyMySQL
* Matplotlib
* Streamlit

### Development Tools

* Git
* GitHub
* VS Code

---

## Project Structure

```text
airport-intelligence-system/

├── api/
├── dashboard/
├── data/
├── ml/
├── notebooks/
├── screenshots/
├── sql/
├── utils/
├── tests/

├── analysis.py
├── README.md
├── requirements.txt
```

---

## Database Design

The project includes a custom relational database that models airport operations.

Main entities include:

* Flights
* Airlines
* Passengers
* Tickets
* Baggage
* Employees
* Employee Assignments

The database was designed using SQL and populated with synthetic data for analysis and reporting purposes.

---

## SQL Reports

The project currently contains analytical SQL reports such as:

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

These reports are stored as reusable SQL files and executed dynamically through Python.

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

---

## Streamlit Dashboard

The project includes an interactive Streamlit dashboard that allows users to explore airport analytics reports.

Current dashboard features:

* Dashboard summary metrics
* Total flights overview
* Delayed flights overview
* Revenue overview
* Static delayed flights visualization
* Interactive report selection using sidebar filters
* Dynamic report tables
* Dynamic report visualizations

Run the dashboard:

```bash
python -m streamlit run dashboard/app.py
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
* Python package structure
* Modular project organization
* Git and GitHub workflows

---

## Future Development

Planned improvements include:

### FastAPI Integration

* REST API endpoints
* Report delivery through API routes
* JSON responses

### Machine Learning Module

* Feature engineering
* Data preprocessing
* Model training
* Model evaluation
* Model persistence
* Prediction API integration

### Project Improvements

* Dashboard enhancements
* Automated testing
* Documentation improvements
* Deployment preparation

---

## Author

Mohammad Sous

AI & Data Science Student

Al-Zaytoonah University of Jordan
