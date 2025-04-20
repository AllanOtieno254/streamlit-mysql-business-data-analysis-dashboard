import streamlit as st
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="my_streamlit",
    port="3306"
    )

c=conn.cursor()

def view_all_data():
    c.execute("SELECT * FROM customers order by id asc")
    data=c.fetchall()
    return data
