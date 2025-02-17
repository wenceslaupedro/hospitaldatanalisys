import pandas as pd

# Load the data
patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_csv("doctors.csv")

# Display the first few rows of each dataset
print("Patients Data:")
print(patients_df.head())

print("\nDoctors Data:")
print(doctors_df.head())