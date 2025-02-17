import pandas as pd

# Load the data
patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_csv("doctors.csv")

# Convert Shift_Start and Shift_End to datetime
doctors_df['Shift_Start'] = pd.to_datetime(doctors_df['Shift_Start'], format='%H:%M').dt.time
doctors_df['Shift_End'] = pd.to_datetime(doctors_df['Shift_End'], format='%H:%M').dt.time

# Analyze doctor availability by department
doctor_availability_by_dept = doctors_df.groupby('Department')['Available'].value_counts().unstack()
print("\nDoctor Availability by Department:")
print(doctor_availability_by_dept)

# Analyze doctor availability by hospital
doctor_availability_by_hospital = doctors_df.groupby('Hospital')['Available'].value_counts().unstack()
print("\nDoctor Availability by Hospital:")
print(doctor_availability_by_hospital)