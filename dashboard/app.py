import streamlit as st
from utils.load_queries import CHARTS, load_report
import requests

#Header
st.set_page_config(
    page_title="Airport Intelligence Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "About": "Airport Intelligence Dashboard built with MySQL, Python, Pandas, and Streamlit."
    }
)
st.title("Airport Intelligence Dashboard")
st.write("This dashboard shows airport analytics using Python, Pandas, SQL, and Streamlit!")

st.divider()
#Metrics summary
flights_df = load_report("Flights per airline")
delays_df = load_report("Delayed flights per airline")
revenue_df = load_report("Total revenue per airline")

col1, col2, col3 = st.columns(3)

col1.metric("Total Flights", f"{flights_df['total_flights'].sum():,}")
col2.metric("Total Delayed Flights", f"{delays_df['delayed_flights'].sum():,}")
col3.metric("Total Revenue", f"${revenue_df['total_revenue'].sum():,.2f}")

st.divider()
#Static important chart

st.subheader("Delayed Flights per Airline")
st.bar_chart(delays_df.set_index("airline")["delayed_flights"])
st.caption("Shows which airlines have the highest number of delayed flights")
#sidebar/explorer
st.sidebar.title("Dashboard Filters")

explorer_charts = {}

for report_name in CHARTS:
    if report_name != "Delayed flights per airline":
        explorer_charts[report_name] = CHARTS[report_name]

selected_report = st.sidebar.selectbox(
    "Select a report:",
    list(explorer_charts.keys())
)

st.divider()
#Load the DataFrame for the selected report
df = load_report(selected_report)

#Show selected report title and table
st.subheader(selected_report)
st.caption("Use the sidebar on the left to choose a report.")
st.dataframe(df.head(10))

#Get chart columns and display chart
x_col, y_col = explorer_charts[selected_report]
st.bar_chart(df.set_index(x_col)[y_col])
st.caption(f"Bar chart showing {y_col} grouped by {x_col}.")

st.divider()

# ML Prediction Section
st.subheader("Flight Delay Prediction")
st.caption("Enter flight details to predict whether the flight may be delayed or not.")

with st.form("delay_prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        airline = st.selectbox(
            "Airline",
            ["Flynas", "MEA", "EgyptAir", "Saudi", "Royal Jordanian", "Emirates", "Flyadeal"]
        )

        origin = st.selectbox(
            "Origin",
            ["Amman", "Cairo", "Dubai", "Riyadh", "Aqaba"]
        )

        destination = st.selectbox(
            "Destination",
            ["Amman", "Cairo", "Dubai", "Riyadh", "Aqaba"]
        )

        gate_id = st.text_input("Gate ID", value="A0009")

    with col2:
        departure_hour = st.number_input(
            "Departure Hour",
            min_value=0,
            max_value=23,
            value=0
        )

        departure_day_of_week = st.number_input(
            "Departure Day of Week",
            min_value=1,
            max_value=7,
            value=2
        )

        tickets_sold = st.number_input(
            "Tickets Sold",
            min_value=0,
            value=20
        )

    with col3:
        average_ticket_price = st.number_input(
            "Average Ticket Price",
            min_value=0.0,
            value=122.13
        )

        employee_count = st.number_input(
            "Employee Count",
            min_value=0,
            value=4
        )

        baggage_count = st.number_input(
            "Baggage Count",
            min_value=0,
            value=30
        )

        total_baggage_weight = st.number_input(
            "Total Baggage Weight",
            min_value=0.0,
            value=1735.92
        )

    submitted = st.form_submit_button("Predict Delay")

if submitted:
    flight_data = {
        "airline": airline,
        "origin": origin,
        "destination": destination,
        "gate_id": gate_id,
        "departure_hour": departure_hour,
        "departure_day_of_week": departure_day_of_week,
        "tickets_sold": tickets_sold,
        "average_ticket_price": average_ticket_price,
        "employee_count": employee_count,
        "baggage_count": baggage_count,
        "total_baggage_weight": total_baggage_weight
    }

    response = requests.post(
        "http://127.0.0.1:8000/api/predictions/delay",
        json=flight_data
    )

    if response.status_code == 200:
        result = response.json()

        st.success(f"Prediction: {result['prediction']}")
        st.metric(
            "Delay Probability",
            f"{result['delay_probability'] * 100:.2f}%"
        )
    else:
        st.error("Prediction request failed. Make sure the FastAPI server is running.")