import pandas as pd

# Load the data
patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_csv("doctors.csv")

# Convert Visit_Date to datetime
patients_df['Visit_Date'] = pd.to_datetime(patients_df['Visit_Date'])

# Extract day of the week and hour from Visit_Time
patients_df['Day_of_Week'] = patients_df['Visit_Date'].dt.day_name()
patients_df['Hour'] = pd.to_datetime(patients_df['Visit_Time']).dt.hour

# Analyze patient inflow by day of the week
patient_inflow_by_day = patients_df['Day_of_Week'].value_counts().sort_index()
print("Patient Inflow by Day of the Week:")
print(patient_inflow_by_day)

# Analyze patient inflow by hour
patient_inflow_by_hour = patients_df['Hour'].value_counts().sort_index()
print("\nPatient Inflow by Hour:")
print(patient_inflow_by_hour)

# Analyze patient inflow by department
patient_inflow_by_dept = patients_df['Department'].value_counts()
print("\nPatient Inflow by Department:")
print(patient_inflow_by_dept)