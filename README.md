# 📊 Business Data Analytics Dashboard

This is an interactive Streamlit dashboard designed to visualize and analyze business data such as employee salaries, departmental distribution, and demographic statistics. It integrates with a MySQL database and offers real-time filtering and graphical insights.

---

## 🚀 Features

- 📁 Loads data directly from a **MySQL database**
- 🧠 Intelligent filtering using **Streamlit Sidebar**
- 📊 Interactive **Pie Chart** showing Department-wise salary distribution
- 📉 **Line Graph** displaying salary trends across different countries
- 📈 **Bar Chart** showcasing average salaries by department
- 🧾 **Expandable Table** to explore raw data
- 📐 Key business metrics (Total Customers, Max Salary, Total Annual Salary)
- 📱 Fully responsive layout with custom CSS for enhanced UX

---


---

## 🧪 Tech Stack

- **Python**
- **Streamlit**
- **MySQL**
- **Pandas**
- **Plotly Express**
- **NumPy**
- **streamlit-option-menu**
- **streamlit-extras**

---

## 📌 Topics Covered

- Data filtering using `query()`
- Plotting charts with Plotly (Pie, Bar, Line)
- SQL Integration with `mysql.connector`
- Dynamic UI generation with Streamlit Widgets
- Metric visualizations with `streamlit_extras.metric_cards`
- Modular programming for clean structure
- Custom CSS integration for UI improvements

---

## 🖼️ Preview

![Dashboard Preview](images/dashboard-preview.png)

---


---

## 📦 2. Install Dependencies

To run this project locally, follow these steps:

### 🔧 Create and activate a virtual environment (recommended)

python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

### installing Required Libraries
pip install -r requirements.txt
pip install mysql-connector-python
pip install streamlit-option-menu
pip install streamlit-extras
pip install streamlit
pip install pandas
pip install plotly

### 💾 3. Setup MySQL Database
Install MySQL Server on your local machine.

Create a database named my_streamlit.

Import the provided customers.csv into a table named customers.

You can use this SQL structure as a reference:

CREATE TABLE customers (
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



## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/business-data-analytics-dashboard.git
cd business-data-analytics-dashboard


---

Would you like me to also generate:

- ✅ A `requirements.txt` file?
- ✅ A custom `LICENSE` file (MIT or others)?
- ✅ A sample `.sql` dump file from your CSV?

Let me know!



























