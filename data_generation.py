import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

# Function to generate a random date within a specified range.
def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    return start_date + timedelta(days=random_number_of_days)

# Function to generate a random name for a hub.
def generate_hub_name():
    prefixes = ['North', 'South', 'East', 'West', 'Central']
    suffixes = ['Wellness', 'Health', 'Care', 'Therapy', 'Healing', 'Clinic', 'Center']
    middle_parts = ['Valley', 'Mountain', 'River', 'City', 'Metro', 'Urban', 'Suburban']
    return f"{random.choice(prefixes)} {random.choice(middle_parts)} {random.choice(suffixes)}"

# Function to generate a realistic number of sessions attended by a patient.
def generate_sessions_attended():
    if random.random() < 0.1:  # 10% chance for extended engagement
        return random.randint(12, 20)
    else:
        return random.randint(1, 10)

# Parameters
states = ['CA', 'FL', 'TX', 'AZ']
hub_names = [generate_hub_name() for _ in range(20)]
patient_id_length = 8
target_rows = 10000
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 12, 31)

# Adjusted revenue and cost parameters
revenue_per_session_adjusted = 120
cost_per_referral_adjusted_range = (200, 300)

# Data generation
data = []
for _ in range(target_rows):
    state = random.choice(states)
    hub = random.choice(hub_names)
    doctor_id = "DR_" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    patient_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=patient_id_length))
    referral_time = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')
    cost_per_referral_adjusted = random.randint(*cost_per_referral_adjusted_range)
    conversion_status = "Yes" if np.random.rand() < 0.4 else "No"
    sessions_attended = generate_sessions_attended() if conversion_status == "Yes" else 0
    revenue = sessions_attended * revenue_per_session_adjusted
    cost = cost_per_referral_adjusted
    net_revenue = revenue - cost
    data.append([state, hub, doctor_id, patient_id, conversion_status, sessions_attended, revenue, cost, net_revenue, referral_time])

# Create DataFrame and export to CSV
df = pd.DataFrame(data, columns=['State', 'Hub', 'Doctor_ID', 'Patient_ID', 'Conversion_Status', 'Sessions_Attended', 'Revenue', 'Cost', 'Net_Revenue', 'Referral_Time'])
csv_filename = 'telehealth_startup_dummy_data.csv'
df.to_csv(csv_filename, index=False)

print(f"CSV file generated: {csv_filename}")
