Project Title: Hospital Resource Management Analysis

Project Overview
This project analyzes hospital data to identify patterns in patient inflow and doctor availability. The goal is to address the issue of doctor shortages during specific times, weeks, or months by proposing solutions such as resource sharing between hospitals or dynamic scheduling.

Datasets
The project uses two main datasets:

•	Patients Dataset: Contains information about patient visits.

•	Doctors Dataset: Contains information about doctor schedules and availability.

1. Patients Dataset
This dataset contains details about patient visits to the hospital.

Fields (Columns):
Patient_ID: Unique identifier for each patient (e.g., P001, P002).
Visit_Date: Date of the patient's visit (format: YYYY-MM-DD).
Visit_Time: Time of the patient's visit (format: HH:MM in 24-hour format).
Department: Department visited by the patient (e.g., Emergency, Pediatrics, Cardiology).
Severity: Severity of the patient's condition (e.g., Low, Medium, High).
Wait_Time: Time the patient waited before being attended (in minutes).
Treatment_Time: Time taken for treatment (in minutes).
Outcome: Outcome of the visit (e.g., Admitted, Discharged, Referred).
Hour: Hour of the day extracted from Visit_Time (e.g., 14 for 2:00 PM).
Day_of_Week: Day of the week extracted from Visit_Date (e.g., Monday, Tuesday).

Example Data:
 

2. Doctors Dataset
This dataset contains details about doctors' schedules and availability.

Fields (Columns):
Doctor_ID: Unique identifier for each doctor (e.g., D001, D002).
Name: Doctor's name (e.g., Dr. Smith).
Department: Department they work in (e.g., Emergency, Pediatrics).
Shift_Start: Start time of their shift (format: HH:MM in 24-hour format).
Shift_End: End time of their shift (format: HH:MM in 24-hour format).
Available: Whether the doctor is available during their shift (e.g., Yes, No).
Hospital: Hospital they belong to (e.g., Hospital A, Hospital B).

Example Data:
 

Analysis Performed
•	Patient Inflow Analysis:
	Analyzed patient inflow by hour, day of the week, and department.
	Identified peak hours and days with the highest patient inflow.

•	Doctor Availability Analysis:
	Analyzed doctor availability by department and hospital.
	Identified shortages during peak hours.

•	Proposed Solutions:
	Suggested resource sharing between hospitals.
	Proposed dynamic scheduling to align doctor shifts with patient inflow.

Visualizations
•	Patient Inflow by Hour:
•	A bar chart showing the number of patients visiting the hospital each hour.

•	Patient Inflow by Day of the Week:
•	A bar chart showing the number of patients visiting the hospital each day of the week.

•	Doctor Availability by Department:
•	A bar chart showing the number of available doctors in each department.

How to Use the Code
•	Generate Data:
Run the data generation script to create synthetic patient and doctor data.
Example: python generate_data.py

•	Analyze Data:
Run the analysis script to perform exploratory data analysis (EDA) and generate visualizations.
Example: python analyze_data.py

•	View Results:
Check the generated visualizations in the plots/ folder.
Review the analysis results in the results/ folder.

Libraries:
•	Pandas: Data manipulation and analysis.
•	Matplotlib: Data visualization
•	Seaborn: Statistical data visualization.
•	Faker: random data generation.



Name: Pedro Brito Wenceslau

Email: pedro.wenceslau@gmail.com

GitHub: https://github.com/wenceslaupedro

