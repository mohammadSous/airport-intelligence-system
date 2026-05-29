import streamlit as st
from utils.load_queries import CHARTS, load_report

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
