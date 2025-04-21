# 📊 Business Data Analytics Dashboard

This is an interactive Streamlit dashboard designed to visualize and analyze business data such as employee salaries, departmental distribution, and demographic statistics. It integrates with a MySQL database and offers real-time filtering and graphical insights.
![homepage](https://github.com/user-attachments/assets/29469c56-6ddc-4a20-9c35-3cd6fe212a9c)

---

## 🚀 Features

- 📁 Loads data directly from a **MySQL database**
- 
- 🧠 Intelligent filtering using **Streamlit Sidebar**
- 
- 📊 Interactive **Pie Chart** showing Department-wise salary distribution
- 
- 📉 **Line Graph** displaying salary trends across different countries
- 
- 📈 **Bar Chart** showcasing average salaries by department
- 
- 🧾 **Expandable Table** to explore raw data
- 
- 📐 Key business metrics (Total Customers, Max Salary, Total Annual Salary)
- 
- 📱 Fully responsive layout with custom CSS for enhanced UX
- 

## 🧪 Tech Stack

- **Python**
- 
- **Streamlit**
- 
- **MySQL**
- 
- **Pandas**
- 
- **Plotly Express**
- 
- **NumPy**
- 
- **streamlit-option-menu**
- 
- **streamlit-extras**
- 

## 📌 Topics Covered

- Data filtering using `query()`
- 
- Plotting charts with Plotly (Pie, Bar, Line)
- 
- SQL Integration with `mysql.connector`
- 
- Dynamic UI generation with Streamlit Widgets
- 
- Metric visualizations with `streamlit_extras.metric_cards`
- 
- Modular programming for clean structure
- 
- Custom CSS integration for UI improvements

---

## 🖼️ Preview

![table](https://github.com/user-attachments/assets/c3c98666-1d88-44f9-b6cd-dcfe4da3953e)

![table description](https://github.com/user-attachments/assets/931f233e-3004-48ab-a147-1e72edb186ac)

---


## 📥 Installing Required Libraries

pip install -r requirements.txt

pip install mysql-connector-python

pip install streamlit-option-menu

pip install streamlit-extras

pip install streamlit

pip install pandas

pip install plotly

## 💾 3. Setup MySQL Database

Install MySQL Server on your local machine.

Create a database named my_streamlit.

Import the provided customers.csv into a table named customers.

You can use this SQL structure as a reference:

CREATE TABLE customers 

(

    EEID INT,
    
    FullName VARCHAR(100),
    
    JobTitle VARCHAR(100),
    
    Department VARCHAR(100),
    
    BusinessUnit VARCHAR(100),
    
    Gender VARCHAR(10),
    
    Ethnicity VARCHAR(50),
    
    Age INT,
    
    HireDate DATE,
    
    AnnualSalary FLOAT,
    
    Bonus FLOAT,
    
    Country VARCHAR(100),
    
    City VARCHAR(100),
    
    id INT PRIMARY KEY
);




## 📦 2. Install Dependencies

To run this project locally, follow these steps:

### 🔧 Create and activate a virtual environment (recommended)

```bash
python -m venv venv

# For Linux/Mac
source venv/bin/activate      

# For Windows
venv\Scripts\activate
