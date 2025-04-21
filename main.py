# Import necessary libraries for building the Streamlit dashboard
import streamlit as st  # Core Streamlit library for web app creation
import pandas as pd  # For data manipulation and analysis
import plotly.express as px  # For creating interactive visualizations
import plotly.subplots as sp  # For creating subplot charts (not used in the script though)
import numpy as np  # For numerical operations

# Import database connection and function to retrieve data
from mysql_con import *  # Custom script to fetch data from MySQL

# Set the basic configuration for the Streamlit page
st.set_page_config(page_title="Business Data Analysis", page_icon="📊", layout="wide")

# Display the dashboard title and description
st.title("Business Data Analysis Dashboard")
st.markdown("This dashboard provides insights into business data, including sales, customer demographics, and product performance.")

# Load and apply custom CSS styles from a local file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Fetch data from the database using a custom function
result = view_all_data()

# Convert fetched data into a pandas DataFrame with defined column names
df = pd.DataFrame(result, columns=[
    "EEID", "FullName", "JobTitle", "Department", "BusinessUnit", "Gender", "Ethnicity", 
    "Age", "HireDate", "AnnualSalary", "Bonus", "Country", "City", "id"
])

# Sidebar filters to narrow down the dataset by Department
st.sidebar.header("Filter Department")
department = st.sidebar.multiselect(
    label="Filter Department",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
)

# Sidebar filters to narrow down the dataset by Gender
st.sidebar.header("Filter Job Title")
Gender = st.sidebar.multiselect(
    label="Filter Job Title",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

# Sidebar filters to narrow down the dataset by Country
st.sidebar.header("Filter Country")
country = st.sidebar.multiselect(
    label="Filter Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

# Sidebar filters to narrow down the dataset by Business Unit
st.sidebar.header("Business Unit")
businessUnit = st.sidebar.multiselect(
    label="Business Unit",
    options=df["BusinessUnit"].unique(),
    default=df["BusinessUnit"].unique()
)

# Filter the DataFrame based on selected sidebar filters
df_selection = df.query(
    "Department==@department & Gender==@Gender & Country==@country & BusinessUnit==@businessUnit"
)

# Define a function to show metric cards
def metrics():
    from streamlit_extras.metric_cards import style_metric_cards  # Import utility to style metrics
    col1, col2, col3 = st.columns(3)  # Create three columns

    # Display key business metrics
    col1.metric(label="Total Customers", value=df_selection.id.count(), delta="All Customers")
    col2.metric(label="Annual Salary", value=f"{df_selection.AnnualSalary.sum():,.0f}", delta="Total Annual Salary")
    col3.metric(label="Max Annual Salary", value=f"{df_selection.AnnualSalary.max():,.0f}", delta="Max Salary")
    
    # Style the metric cards
    style_metric_cards(background_color="#071021", border_left_color="#1f66bd")

# Call the metrics function
metrics()

# Divide the main area into three columns for visualizations
div1, div2, div3 = st.columns(3)

# Function to display a pie chart of Annual Salary by Department
def pie():
    with div1:
        fig = px.pie(
            df_selection,
            values="AnnualSalary",
            names="Department",
            title="Department-wise Salary Distribution",
        )
        fig.update_layout(legend_title="Department", legend_y=0.9)
        fig.update_traces(textinfo="percent+label", textposition="inside")
        st.plotly_chart(fig, use_container_width=True)

# Function to display a bar chart of Annual Salary by Department
def bar():
    with div2:
        fig = px.bar(
            df_selection,
            x="Department",
            y="AnnualSalary",
            text_auto=".2s",
            color="Department",
            title="Average Annual Salary by Department",
            text="AnnualSalary",
        )
        fig.update_layout(legend_title="Department", legend_y=0.9)
        fig.update_traces(textfont_size=18, textangle=0, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig, use_container_width=True)

# Function to display a line chart of total Annual Salary by Country
def line_salary_by_country():
    with div3:
        salary_country = df_selection.groupby("Country")["AnnualSalary"].sum().reset_index()

        fig = px.line(
            salary_country,
            x="Country",
            y="AnnualSalary",
            title="Annual Salary Trend by Country",
            markers=True,
            line_shape="linear"
        )
        fig.update_layout(
            xaxis_title="Country",
            yaxis_title="Total Annual Salary",
            title_x=0.3,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
        )
        st.plotly_chart(fig, use_container_width=True)

# Function to display a table with column selection
def table():
    with st.expander("My Database Table"):
        shwdata = st.multiselect("Filter Dataset", df_selection.columns, default=[
            "EEID", "FullName", "JobTitle", "Department", "BusinessUnit", "Gender", "Ethnicity",
            "Age", "HireDate", "AnnualSalary", "Bonus", "Country", "City", "id"
        ])
        st.dataframe(df_selection[shwdata], use_container_width=True)

# Import option_menu for sidebar navigation
from streamlit_option_menu import option_menu

# Create a sidebar navigation menu with Home and Table options
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Table"],
        icons=["house", "book"],
        default_index=0,
        orientation="vertical",
    )

# Conditional rendering based on selected menu option
if selected == "Home":
    pie()  # Show pie chart
    bar()  # Show bar chart
    line_salary_by_country()  # Show line chart

elif selected == "Table":
    table()  # Show data table
    st.dataframe(df_selection.describe().T)  # Show summary statistics
