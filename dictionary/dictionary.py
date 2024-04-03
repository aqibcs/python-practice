import pandas as pd

# Sample data for employees
employees = {
    'Employee ID': [101, 102, 103, 104, 105],
    'Name': [
        'John Doe', 'Jane Smith', 'Michael Johnson', 'Emily Davis',
        'David Brown'
    ],
    'Department': ['Sales', 'Marketing', 'Finance', 'HR', 'IT'],
    'Salary': [60000, 65000, 70000, 55000, 75000]
}

# Creating the DataFrame
df = pd.DataFrame(employees)
print(df)
