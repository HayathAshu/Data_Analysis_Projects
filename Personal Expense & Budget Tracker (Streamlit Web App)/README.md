# 💰 Personal Expense & Budget Tracker (Streamlit Web App)

## 📌 Problem Statement

Managing personal finances manually can be difficult and unorganized. Many individuals struggle to:

- Track daily expenses
- Set monthly budgets
- Monitor overspending
- Analyze spending patterns

This project aims to solve this problem by building a simple and interactive **Personal Expense & Budget Tracker Web Application** using Python and Streamlit.

---

## 🎯 Project Objective

To develop a user-friendly web application that allows users to:

- Add and store daily expenses
- Set monthly budgets for different categories
- Compare spending against budgets
- Filter expenses by date range
- Visualize category-wise spending using charts

---

## ⚙️ How This Project Works

The application is built using Streamlit and follows this workflow:

### 1️⃣ Add Expense
- User enters:
  - Date
  - Category (Food, Travel, Shopping, etc.)
  - Amount
- The expense is stored in a CSV file (`expenses.csv`).

### 2️⃣ Set Budget
- User sets a monthly budget for each category.
- Budget data is stored in (`budgets.csv`).

### 3️⃣ Dashboard
The dashboard displays:
- Filtered expenses (based on selected date range)
- Category-wise total spending
- Bar chart visualization
- Budget vs Actual spending comparison
- Over-budget alerts
- Delete option for removing unwanted expense entries

---

## 🛠️ Tools & Technologies Used

### 🔹 1. Python
- Core programming language used to build the application logic.

### 🔹 2. Streamlit
- Used to create the interactive web interface.
- Handles user inputs, buttons, navigation, and layout.

### 🔹 3. Pandas
- Used for:
  - Data storage and manipulation
  - Groupby operations
  - Date filtering
  - Merging expense and budget data

### 🔹 4. Matplotlib
- Used to generate bar charts for visualizing category-wise spending.

### 🔹 5. CSV Files
- `expenses.csv` → Stores all expense records.
- `budgets.csv` → Stores monthly budget data.
- Acts as a lightweight database for this application.

---

## 📊 Features Implemented

✔ Add new expenses  
✔ Set monthly budgets  
✔ Date range filtering  
✔ Category-wise expense summary  
✔ Budget vs Spending comparison  
✔ Over-budget alerts  
✔ Delete expense functionality  
✔ Interactive dashboard  

---

## 📂 Project Structure
```
expense_tracker_app/
│
├── app.py
├── expenses.csv
├── budgets.csv
└── README.md
```

---

## ▶️ How to Run the Project

1. Clone the repository:
```
git clone <your-repo-link>
```

2. Navigate to project folder:
```
cd expense_tracker_app
```

3. Install required libraries:
```
pip install streamlit pandas matplotlib
```

4. Run the application:
```
streamlit run app.py
```


---

## 🚀 Future Improvements

- User authentication system
- Database integration (MySQL / PostgreSQL)
- Monthly summary reports
- Downloadable expense reports (PDF/Excel)
- Multi-user support

---

## 👨‍💻 Author

**Mohammed Hayath RK**  
Passionate about Python, Data Analytics, and Web Application Development.

---

## 📌 Conclusion

This project demonstrates practical implementation of:

- Data handling using Pandas
- Interactive dashboard creation using Streamlit
- Data visualization
- Budget analysis logic
- Real-world problem solving using Python

It serves as a complete beginner-to-intermediate level data application project suitable for portfolios and internship evaluations.
