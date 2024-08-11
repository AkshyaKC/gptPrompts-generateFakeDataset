import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Define the number of rows
num_rows = 10000

# Define possible values for categorical columns
genders = ['Male', 'Female']
chronic_conditions = ['Diabetes', 'Hypertension', 'Heart Disease', 'None']
insurance_types = ['Private', 'Medicare', 'Medicaid', 'Uninsured']
discharge_instructions = ['Follow-up in 1 week', 'Take medications as prescribed', 'Monitor symptoms', 'None']
common_medications = [
    "Aspirin", "Metformin", "Lisinopril", "Simvastatin", "Amoxicillin",
    "Ibuprofen", "Omeprazole", "Levothyroxine", "Metoprolol", "Atorvastatin",
    "Albuterol", "Gabapentin", "Amlodipine", "Hydrochlorothiazide", "Losartan",
    "Acetaminophen", "Furosemide", "Prednisone", "Montelukast", "Clopidogrel",
    "Doxycycline", "Fluticasone", "Spironolactone", "Citalopram", "Sertraline"
]

# Define categorized procedures
procedures = {
    "Diagnostic Tests": ["Blood Test", "X-ray", "MRI Scan", "CT Scan", "Ultrasound"],
    "Surgeries": ["Appendectomy", "Cholecystectomy", "Coronary Artery Bypass Surgery", "Hip Replacement", "Knee Arthroscopy"],
    "Therapeutic Procedures": ["Chemotherapy", "Radiation Therapy", "Dialysis", "Physical Therapy"],
    "Minor Procedures": ["Biopsy", "Endoscopy", "Colonoscopy", "Skin Lesion Removal", "Wound Care"]
}

# Create a function to generate a list of random chronic conditions
def random_chronic_conditions():
    return random.sample(chronic_conditions, k=random.randint(1, 3))

# Create a function to generate a list of random medications
def random_medications():
    return random.sample(common_medications, k.random.randint(1, 5))

# Create a function to generate a list of random procedures with categories
def random_procedures():
    all_procedures = []
    for category, items in procedures.items():
        selected_procedures = random.sample(items, k=random.randint(0, 3))
        for procedure in selected_procedures:
            all_procedures.append(f"{category}: {procedure}")
    return all_procedures

# Generate the data
data = {
    'Patient ID': [fake.uuid4() for _ in range(num_rows)],
    'Age': [random.randint(1, 100) for _ in range(num_rows)],
    'Gender': [random.choice(genders) for _ in range(num_rows)],
    'Chronic Conditions': [', '.join(random_chronic_conditions()) for _ in range(num_rows)],
    'Past Hospitalizations': [random.randint(0, 10) for _ in range(num_rows)],
    'Medications': [', '.join(random_medications()) for _ in range(num_rows)],
    'Procedures': [', '.join(random_procedures()) for _ in range(num_rows)],
    'Length of Stay': [random.randint(1, 30) for _ in range(num_rows)],
    'Follow-up Appointments': [random.randint(0, 5) for _ in range(num_rows)],
    'Discharge Instructions': [random.choice(discharge_instructions) for _ in range(num_rows)],
    'Insurance Type': [random.choice(insurance_types) for _ in range(num_rows)],
    'Access to Care': [random.choice(['Good', 'Fair', 'Poor']) for _ in range(num_rows)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to a CSV file
df.to_csv('patient_medical_history.csv', index=False)