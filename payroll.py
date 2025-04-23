import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime

# Initialize SQLite Database
conn = sqlite3.connect('payroll.db')
cursor = conn.cursor()

# Create tables if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT,
        basic_salary REAL,
        tax_rate REAL,
        bank_account TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS payroll (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        employee_id INTEGER,
        month TEXT,
        year INTEGER,
        basic_salary REAL,
        allowances REAL,
        deductions REAL,
        net_salary REAL,
        FOREIGN KEY (employee_id) REFERENCES employees (id)
    )
''')
conn.commit()

# Streamlit App
st.title("💰 Payroll Management System")

# Sidebar Menu
menu = st.sidebar.selectbox(
    "Menu",
    ("Add Employee", "View Employees", "Process Payroll", "View Payslips")
)

# Function to add an employee
if menu == "Add Employee":
    st.subheader("Add New Employee")
    with st.form("employee_form"):
        name = st.text_input("Full Name")
        position = st.text_input("Position")
        basic_salary = st.number_input("Basic Salary ($)", min_value=0.0)
        tax_rate = st.number_input("Tax Rate (%)", min_value=0.0, max_value=30.0)
        bank_account = st.text_input("Bank Account Number")
        
        if st.form_submit_button("Save Employee"):
            cursor.execute(
                "INSERT INTO employees (name, position, basic_salary, tax_rate, bank_account) VALUES (?, ?, ?, ?, ?)",
                (name, position, basic_salary, tax_rate, bank_account)
            )
            conn.commit()
            st.success("Employee added successfully!")

# Function to view employees
elif menu == "View Employees":
    st.subheader("Employee Records")
    employees = pd.read_sql("SELECT * FROM employees", conn)
    st.dataframe(employees)

# Function to process payroll
elif menu == "Process Payroll":
    st.subheader("Run Payroll")
    employees = pd.read_sql("SELECT * FROM employees", conn)
    
    if not employees.empty:
        selected_employee = st.selectbox("Select Employee", employees["name"])
        employee_data = employees[employees["name"] == selected_employee].iloc[0]
        
        with st.form("payroll_form"):
            month = st.selectbox("Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
            year = st.number_input("Year", min_value=2020, max_value=2030, value=datetime.now().year)
            allowances = st.number_input("Allowances ($)", min_value=0.0)
            deductions = st.number_input("Deductions ($)", min_value=0.0)
            
            if st.form_submit_button("Calculate Salary"):
                basic_salary = employee_data["basic_salary"]
                tax_amount = (basic_salary + allowances) * (employee_data["tax_rate"] / 100)
                net_salary = (basic_salary + allowances) - (tax_amount + deductions)
                
                cursor.execute(
                    "INSERT INTO payroll (employee_id, month, year, basic_salary, allowances, deductions, net_salary) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (employee_data["id"], month, year, basic_salary, allowances, deductions, net_salary)
                )
                conn.commit()
                st.success(f"Payroll processed! Net Salary: ${net_salary:.2f}")

# Function to view payslips
elif menu == "View Payslips":
    st.subheader("Payslip Records")
    payroll_data = pd.read_sql(
        "SELECT payroll.*, employees.name FROM payroll JOIN employees ON payroll.employee_id = employees.id",
        conn
    )
    st.dataframe(payroll_data)
    
    # Export to Excel
    if st.button("Export to Excel"):
        payroll_data.to_excel("payroll_records.xlsx", index=False)
        st.success("Exported to Excel!")

# Close DB connection
conn.close()
