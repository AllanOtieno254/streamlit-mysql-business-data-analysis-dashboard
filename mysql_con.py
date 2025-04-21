# Import the Streamlit library for building interactive web apps
import streamlit as st

# Import the MySQL connector to interact with MySQL databases
import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",      # Hostname of the MySQL server (localhost means local machine)
    user="root",           # Username to access the MySQL database (default is "root" for local setups)
    password="",           # Password for the MySQL user (empty string if no password is set)
    database="my_streamlit", # The specific database you want to connect to
    port="3306"            # Port number where MySQL server is running (default is 3306)
)

# Create a cursor object to interact with the database (used to execute SQL queries)
c = conn.cursor()

# Define a function to fetch all data from the 'customers' table
def view_all_data():
    # Execute SQL query to select all rows from 'customers' table ordered by 'id' in ascending order
    c.execute("SELECT * FROM customers ORDER BY id ASC")
    
    # Fetch all rows returned by the query and store in 'data'
    data = c.fetchall()
    
    # Return the fetched data to the caller
    return data
