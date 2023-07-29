import csv
import statistics
from collections import Counter
import pandas as pd

def Average(coloumn):
    return sum(coloumn) / (len(coloumn))

data = pd.read_csv('Employees.csv')
emp_data = pd.DataFrame(data)

# Remove any duplicates in the table
emp_data.drop_duplicates(subset='Name ',keep='first',inplace=True)

# Remove any decimal places in the Age column
emp_data['Age'] = emp_data['Age'].astype('int')

# Convert the USD salary to EGP
emp_data['Salary(USD)'] = emp_data['Salary(USD)']*(30.90)

print(emp_data)

# Count the number of Females and Males in the Gender coloumn
Counter_Male_Female=list(Counter(emp_data['Gender']).values())

# Ration between males and female employees
Ration_M_F= Counter_Male_Female[0]/Counter_Male_Female[1]

print("Average age = ",Average(emp_data['Age']))

print("Median Salaries = ",statistics.median(emp_data['Salary(USD)']))

print("Ration between males and female employees = ", Counter_Male_Female[0]/Counter_Male_Female[1])

filename = "New Employees.csv"

emp_data.to_csv(filename,index=False)
