# **Payroll Management System with Python & Streamlit**  

![Payroll System Demo](https://via.placeholder.com/600x400?text=Payroll+System+Demo)  

A **simple yet powerful payroll management system** built with Python, Streamlit, and SQLite. This system allows businesses to manage employee records, calculate salaries, generate payslips, and export payroll data.  

---

## **Features**  
✅ **Employee Management** – Add, view, and manage employee details.  
✅ **Payroll Processing** – Automatically calculates salary, taxes, deductions, and net pay.  
✅ **Payslip Generation** – View and export payroll records.  
✅ **Excel Export** – Download payroll data in `.xlsx` format.  
✅ **SQLite Database** – Securely stores employee and payroll records.  

---

## **Technologies Used**  
- **Frontend**: `Streamlit`  
- **Backend**: `Python`  
- **Database**: `SQLite`  
- **Data Handling**: `Pandas`  
- **Excel Export**: `OpenPyXL`  

---

## **Installation & Setup**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/yourusername/payroll-system.git
cd payroll-system
```

### **2. Install Dependencies**  
```sh
pip install streamlit pandas openpyxl
```

### **3. Run the Application**  
```sh
streamlit run payroll_system.py
```

The app will open in your default browser at **`http://localhost:8501`**.  

---

## **How to Use**  

### **1. Add Employees**  
- Go to **"Add Employee"** in the sidebar.  
- Enter employee details (name, position, salary, tax rate, bank account).  
- Click **"Save Employee"**.  

### **2. View Employees**  
- Navigate to **"View Employees"** to see all records.  

### **3. Process Payroll**  
- Select an employee, month, and year.  
- Enter allowances and deductions.  
- Click **"Calculate Salary"** to generate net pay.  

### **4. View & Export Payslips**  
- Go to **"View Payslips"** to see payroll history.  
- Click **"Export to Excel"** to download records.  

---

## **Project Structure**  
```
payroll-system/
├── payroll_system.py       # Main application code
├── payroll.db             # SQLite database (auto-created)
├── payroll_records.xlsx    # Generated Excel file (after export)
└── README.md
```

---

## **Future Enhancements**  
🔹 **User Authentication** (Secure login for HR)  
🔹 **Automated Tax Rules** (Country-specific calculations)  
🔹 **Email Payslips** (Send payslips via email)  
🔹 **Advanced Analytics** (Salary trends, tax reports)  

---

## **Contributing**  
Feel free to fork, improve, and submit a PR!  

---

## **License**  
MIT  

---

**Enjoy managing payroll with ease!** 🚀  

--- 

Would you like me to add **screenshots** or a **deployment guide** (e.g., Heroku, Docker)? Let me know! 😊
