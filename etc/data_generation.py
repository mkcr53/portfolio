import pandas as pd
import numpy as np
import random
import string
from datetime import datetime, timedelta

def generate_random_date(start_date, end_date):
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

def generate_hub_name():
    prefixes = ['North', 'South', 'East', 'West', 'Central']
    middles = ['Valley', 'Mountain', 'River', 'City', 'Metro', 'Urban', 'Suburban']
    suffixes = ['Wellness', 'Health', 'Care', 'Therapy', 'Healing', 'Clinic', 'Center']
    return f"{random.choice(prefixes)} {random.choice(middles)} {random.choice(suffixes)}"

def simulate_patient_journey():
    contacted = 1  # Assume all referrals are contacted
    scheduled = 1 if random.random() < 0.6 else 0  # 40-60% are scheduled
    first_session_attended = 1 if scheduled and random.random() < 0.8 else 0  # 70-90% of those scheduled attend their first session
    multiple_sessions_attended = 1 if first_session_attended and random.random() < 0.4 else 0  # 30-50% of those who attend the first session attend multiple sessions
    return contacted, scheduled, first_session_attended, multiple_sessions_attended

states = ['CA', 'FL', 'TX', 'AZ']
hub_names = [generate_hub_name() for _ in range(20)]
num_records = 10000
start_date = datetime(2021, 1, 1)
end_date = datetime(2022, 12, 31)

data = []
for _ in range(num_records):
    state = random.choice(states)
    hub = random.choice(hub_names)
    doctor_id = 'DR_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    patient_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    referral_date = generate_random_date(start_date, end_date).strftime('%Y-%m-%d')
    sessions_attended = random.randint(0, 10)
    revenue = sessions_attended * 100  # Assuming $100 revenue per session
    cost = 200  # Assuming a fixed cost of $200 per referral
    net_revenue = revenue - cost
    journey = simulate_patient_journey()

    record = [state, hub, doctor_id, patient_id, referral_date, sessions_attended, revenue, cost, net_revenue] + list(journey)
    data.append(record)

columns = ['State', 'Hub', 'Doctor_ID', 'Patient_ID', 'Referral_Date', 'Sessions_Attended',
           'Revenue', 'Cost', 'Net_Revenue', 'Contacted', 'Scheduled', 'First Session Attended',
           'Multiple Sessions Attended']

# Main detailed dataset
df = pd.DataFrame(data, columns=columns)
df.to_csv('telehealth_startup_detailed_data.csv', index=False)

# Funnel dataset
funnel_counts = {
    'Contacted': df['Contacted'].sum(),
    'Scheduled': df['Scheduled'].sum(),
    'First Session Attended': df['First Session Attended'].sum(),
    'Multiple Sessions Attended': df['Multiple Sessions Attended'].sum()
}
funnel_df = pd.DataFrame(list(funnel_counts.items()), columns=['Funnel Stage', 'Count'])
funnel_df.to_csv('telehealth_startup_funnel_data.csv', index=False)

print("Detailed data and funnel data successfully generated and saved.")
