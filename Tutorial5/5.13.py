import pandas as pd

def analyze_employee_data():
    employee_data = pd.read_csv("employee.csv")

    print("Employee Data Preview:")
    print(employee_data.head())

    # 1. Print first 7 records from employees file
    print("First 7 Records:")
    print(employee_data.head(7))

    # 2. Print all employee names in alphabetical order
    print("Employee Names in Alphabetical Order:")
    print(employee_data["name"].sort_values().tolist())

    # 3. Find the name of the employee with highest salary
    top_earner = employee_data[employee_data["salary"] == employee_data["salary"].max()]["name"].values[0]
    print("Employee with the Highest Salary:", top_earner)

    # 4. List the names of male employees
    male_staff = employee_data[employee_data["gender"] == "Male"]["name"].tolist()
    print("Male Employees:", male_staff)

    # 5. Display to which all teams employees belong
    unique_teams = employee_data["team"].unique().tolist()
    print("Teams Employees Belong To:", unique_teams)

# Call the function
analyze_employee_data()
