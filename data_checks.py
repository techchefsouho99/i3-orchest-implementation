import pandas as pd
from datetime import datetime

# Load the CSV with index column
df = pd.read_csv("ratings.csv", index_col=False)

# Function to correct errors
def clean_data(row):
    try:
        row['timestamp'] = datetime.strptime(row['timestamp'], "%Y-%m-%dT%H:%M:%S").isoformat()
    except (ValueError, TypeError):
        print('Wrong datetime format:' + row['timestamp'] + " -> " + row['timestamp'] + ":00")
        row['timestamp'] = row['timestamp'] + ":00"

    if pd.isna(row['user_id']) or not isinstance(row['user_id'], (int, float)):
        print("User ID is not known, changed to -1")
        row['user_id'] = -1

    if pd.isna(row['movie_id']) or not isinstance(row['movie_id'], str):
        print("Movie ID is not known, changed to 'unknown_movie'")
        row['movie_id'] = "unknown_movie"

    try:
        row['rating'] = int(row['rating'])
        if row['rating'] < 0 or row['rating'] > 5:
            row['rating'] = 3
    except (ValueError, TypeError):
        return None

    return row

# Apply cleaning
df = df.apply(clean_data, axis=1)

# Drop invalid rows
if len(df) != len(df.dropna()):
    print("Some rows with ratings missing! Dropping those!")
    df = df.dropna().reset_index(drop=True)

print("File's cleaned now!!")

# # Re-add a proper Unnamed: 0 column for format consistency
# df.insert(0, "Unnamed: 0", range(len(df)))

# Save it
# df.to_csv("cleaned_ratings.csv", index=False)
