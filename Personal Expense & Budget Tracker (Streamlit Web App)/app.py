#  Basic Streamlit App Structure

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Expense Tracker", layout="wide")

st.title("💰 Personal Expense & Budget Tracker")

# Ensure CSV files exist
if not os.path.exists("expenses.csv"):
    pd.DataFrame(columns=["Date", "Category", "Amount"]).to_csv("expenses.csv", index=False)

if not os.path.exists("budgets.csv"):
    pd.DataFrame(columns=["Category", "Monthly_Budget"]).to_csv("budgets.csv", index=False)

# Load data
expenses_df = pd.read_csv("expenses.csv")
budgets_df = pd.read_csv("budgets.csv")


# Sidebar Navigation

menu = st.sidebar.selectbox(
    "Navigation",
    ["Add Expense", "Set Budget", "Dashboard"]
)


# Add Expense Page

if menu == "Add Expense":
    st.subheader("➕ Add New Expense")

    date = st.date_input("Select Date")
    category = st.text_input("Enter Category")
    amount = st.number_input("Enter Amount", min_value=0.0)

    if st.button("Add Expense"):
        new_data = pd.DataFrame({
            "Date": [date],
            "Category": [category],
            "Amount": [amount]
        })

        expenses_df = pd.concat([expenses_df, new_data], ignore_index=True)
        expenses_df.to_csv("expenses.csv", index=False)

        st.success("Expense Added Successfully!")


# Set Budget Page

elif menu == "Set Budget":
    st.subheader("📊 Set Monthly Budget")

    category = st.text_input("Category Name")
    budget = st.number_input("Monthly Budget", min_value=0.0)

    if st.button("Save Budget"):
        budgets_df = budgets_df[budgets_df["Category"] != category]

        new_budget = pd.DataFrame({
            "Category": [category],
            "Monthly_Budget": [budget]
        })

        budgets_df = pd.concat([budgets_df, new_budget], ignore_index=True)
        budgets_df.to_csv("budgets.csv", index=False)

        st.success("Budget Saved Successfully!")


# Dashboard Page

elif menu == "Dashboard":
    st.subheader("📈 Expense Dashboard")

    if not expenses_df.empty:
        expenses_df["Date"] = pd.to_datetime(expenses_df["Date"])

        # Date Filter
        start_date = st.date_input("Start Date", expenses_df["Date"].min())
        end_date = st.date_input("End Date", expenses_df["Date"].max())

        filtered_df = expenses_df[
            (expenses_df["Date"] >= pd.to_datetime(start_date)) &
            (expenses_df["Date"] <= pd.to_datetime(end_date))
        ]

        st.write("### Filtered Expenses")

        if not filtered_df.empty:

    # Reset index so we can delete properly
            filtered_df = filtered_df.reset_index()

            selected_index = st.selectbox(
            "Select row to delete",
            filtered_df["index"]
    )

        if st.button("Delete Selected Expense"):
            expenses_df.drop(selected_index, inplace=True)
            expenses_df.to_csv("expenses.csv", index=False)
            st.success("Expense Deleted Successfully!")
            st.experimental_rerun()

            st.dataframe(filtered_df.drop(columns=["index"]))


        # Category-wise spending
        category_summary = filtered_df.groupby("Category")["Amount"].sum().reset_index()

        st.write("### Category-wise Spending")
        st.dataframe(category_summary)

        # Bar Chart
        fig, ax = plt.subplots()
        ax.bar(category_summary["Category"], category_summary["Amount"])
        plt.xticks(rotation=45)
        st.pyplot(fig)

        # Budget Comparison
        if not budgets_df.empty:
            merged = pd.merge(category_summary, budgets_df, on="Category", how="left")
            merged["Remaining"] = merged["Monthly_Budget"] - merged["Amount"]

            st.write("### Budget vs Spending")
            st.dataframe(merged)

            for index, row in merged.iterrows():
                if row["Remaining"] < 0:
                    st.error(f"You exceeded the budget for {row['Category']}!")
    else:
        st.warning("No expenses recorded yet.")

