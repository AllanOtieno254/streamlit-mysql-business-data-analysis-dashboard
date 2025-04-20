import streamlit as st 
import pandas as pd 
import plotly.express as px
import plotly.subplots as sp
import numpy as np

from mysql_con import *

st.set_page_config(page_title="Business Data Analysis", page_icon="📊", layout="wide")
st.title("Business Data Analysis Dashboard")
st.markdown("This dashboard provides insights into business data, including sales, customer demographics, and product performance.")

#call css
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

result=view_all_data()
df=pd.DataFrame(result, columns=[
"EEID",
"FullName",
"JobTitle",
"Department",
"BusinessUnit",
"Gender",
"Ethnicity",
"Age",
"HireDate",
"AnnualSalary",
"Bonus",
"Country",
"City",
"id"
])
#st.dataframe(df) #or you can use st.write(df)


st.sidebar.header("Filter Department")
department=st.sidebar.multiselect(
    label="Filter Department",
    options=df["Department"].unique(),
    default=df["Department"].unique(),
)

st.sidebar.header("Filter Job Title")
Gender=st.sidebar.multiselect(
    label="Filter Job Title",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

st.sidebar.header("Filter Country")
country=st.sidebar.multiselect(
    label="Filter Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

st.sidebar.header("Business Unit")
businessUnit=st.sidebar.multiselect(
    label="Business Unit",
    options=df["BusinessUnit"].unique(),
    default=df["BusinessUnit"].unique()
)

df_selection=df.query(
    "Department==@department & Gender==@Gender & Country==@country & BusinessUnit==@businessUnit"
)

def metrics():
    from streamlit_extras.metric_cards import style_metric_cards
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Total Customers", value=df_selection.id.count(),delta="All Customers")
    col2.metric(label="Annual Salary", value=f"{df_selection.AnnualSalary.sum():,.0f}", delta="Total Annual Salary")
    col3.metric(label="Max Annual Salary", value=f"{df_selection.AnnualSalary.max():,.0f}", delta="Max Salary")
    
    
    style_metric_cards(background_color="#071021",border_left_color="#1f66bd") 
    
metrics()

div1, div2, div3 = st.columns(3)

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

        st.plotly_chart(fig, use_container_width=True)  # no theme param here either

#pie()

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
        fig.update_traces(textfont_size=18,textangle=0, textposition="outside",cliponaxis=False)

        st.plotly_chart(fig, use_container_width=True)  # no theme param here either
#bar()

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

#line_salary_by_country()

def table():
    with st.expander("My Database Table"):
        shwdata = st.multiselect("Filter Dataset", df_selection.columns, default=[
            "EEID",
            "FullName",
            "JobTitle",
            "Department",
            "BusinessUnit",
            "Gender",
            "Ethnicity",
            "Age",
            "HireDate",
            "AnnualSalary",
            "Bonus",
            "Country",
            "City",
            "id"
        ])
        st.dataframe(df_selection[shwdata], use_container_width=True)

#table()

from streamlit_option_menu import option_menu

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Table"],
        icons=["house", "book"],
        default_index=0,
        orientation="vertical",
    )

# Main page content
if selected == "Home":
    pie()
    bar()
    line_salary_by_country()

elif selected == "Table":
    table()
    st.dataframe(df_selection.describe().T)
