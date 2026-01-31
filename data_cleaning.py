print("SCRIPT STARTED")

import pandas as pd
import numpy as np

df = pd.read_csv("raw_data.csv")

print("DATA LOADED")
print(df.head())

df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')
df['last_active_date'] = pd.to_datetime(df['last_active_date'], errors='coerce')

df['subscription_type'] = df['subscription_type'].fillna('Unknown')
df['amount'] = df['amount'].fillna(df['amount'].median())

df['active_days'] = (df['last_active_date'] - df['signup_date']).dt.days

df.to_csv("cleaned_data.csv", index=False)

print("SCRIPT FINISHED SUCCESSFULLY")
