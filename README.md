# Employee Data Cleaning Project

## Project Overview
This project focuses on cleaning and preparing a real-world employee dataset using Python and Pandas.  
The raw data contained formatting issues, missing values, invalid dates, and duplicated headers.

## Dataset Description
The dataset includes the following columns:
- employee_id: Unique ID for each employee
- joining_date: Date the employee joined the company
- last_working_date: Last working date of the employee
- department: Department name
- monthly_salary: Monthly salary in INR

## Problems Identified
- Dataset loaded as a single column due to formatting issues
- Duplicate header row present in data
- Missing values in department and salary
- Invalid and missing dates

## Steps Performed
- Loaded and inspected the dataset
- Fixed delimiter and formatting issues
- Removed duplicate header rows
- Converted columns to appropriate data types
- Handled missing values using logical strategies
- Created a new feature: employee tenure in days
- Saved the cleaned dataset for further analysis

## Tools Used
- Python
- Pandas
- NumPy

## Output Files
- employee_data.csv (raw data)
- cleaned_employee_data.csv (cleaned data)

## Conclusion
The cleaned dataset is now ready for further analysis or modeling. This project demonstrates practical data cleaning and feature engineering skills using Python.# employee-data-cleaning
Data cleaning and feature engineering on employee dataset using Python and Pandas
