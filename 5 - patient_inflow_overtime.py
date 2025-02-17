
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

patients_df = pd.read_csv("patients.csv")
doctors_df = pd.read_csv("doctors.csv")

# Patient inflow by hour
plt.figure(figsize=(10, 6))
sns.countplot(x='Hour', data=patients_df, palette='viridis')
plt.title("Patient Inflow by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Patients")
plt.show()

# Patient inflow by day of the week
plt.figure(figsize=(10, 6))
patients_df['Visit_Date'] = pd.to_datetime(patients_df['Visit_Date'])
patients_df['Day_of_Week'] = patients_df['Visit_Date'].dt.day_name()
sns.countplot(x='Day_of_Week', data=patients_df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='viridis')
plt.title("Patient Inflow by Day of the Week")
plt.xlabel("Day of the Week")
plt.ylabel("Number of Patients")
plt.show()