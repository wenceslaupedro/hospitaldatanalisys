from faker import Faker
import pandas as pd
import random

fake = Faker()

# Generate Patients Data
patients_data = []
for i in range(1000):
    patients_data.append({
        "Patient_ID": f"P{i+1:03}",
        "Visit_Date": fake.date_between(start_date='-30d', end_date='today'),
        "Visit_Time": fake.time(pattern='%H:%M'),
        "Department": random.choice(["Emergency", "Pediatrics", "Cardiology"]),
        "Severity": random.choice(["Low", "Medium", "High"]),
        "Wait_Time": random.randint(5, 60),
        "Treatment_Time": random.randint(10, 120),
        "Outcome": random.choice(["Admitted", "Discharged", "Referred"])
    })

patients_df = pd.DataFrame(patients_data)

# Convert Visit_Time to datetime and extract the hour
patients_df['Hour'] = pd.to_datetime(patients_df['Visit_Time'], format='%H:%M').dt.hour


# Generate Doctors Data
doctors_data = []
for i in range(10):
    doctors_data.append({
        "Doctor_ID": f"D{i+1:03}",
        "Name": fake.name(),
        "Department": random.choice(["Emergency", "Pediatrics", "Cardiology"]),
        "Shift_Start": f"{random.randint(8, 12):02}:00",
        "Shift_End": f"{random.randint(13, 20):02}:00",
        "Available": random.choice(["Yes", "No"]),
        "Hospital": random.choice(["Hospital A", "Hospital B"])
    })

doctors_df = pd.DataFrame(doctors_data)

# Save to CSV (optional)
patients_df.to_csv("patients.csv", index=False)
doctors_df.to_csv("doctors.csv", index=False)

