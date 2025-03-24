import pandas as pd
import os

INPUT_LOG_FILE = "kafka_ratings_log.csv"
OUTPUT_RATINGS_FILE = "ratings.csv"

def extract_ratings_from_log(file_path):
    ratings = []
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue  # Skip malformed logs
            timestamp, user_id, action = parts[:3]

            if "GET /rate/" in action:
                rating_info = action.split("=")
                if len(rating_info) == 2:
                    movie_id = rating_info[0].split("/")[-1]
                    rating = rating_info[1]
                    try:
                        ratings.append((timestamp, user_id, movie_id, int(rating)))
                    except ValueError:
                        continue  # Skip lines with invalid rating
    return ratings

def save_ratings_to_csv(ratings, output_path):
    df_ratings = pd.DataFrame(ratings, columns=["timestamp", "user_id", "movie_id", "rating"])
    # df_ratings.to_csv(output_path, index=True, index_label="")
    print(f"✅ Saved {len(df_ratings)} ratings to {output_path}")

def main():
    if not os.path.exists(INPUT_LOG_FILE):
        print(f"❌ Input log file not found: {INPUT_LOG_FILE}")
        return
    
    ratings = extract_ratings_from_log(INPUT_LOG_FILE)
    if not ratings:
        print("⚠️ No ratings extracted from the log.")
        return

    save_ratings_to_csv(ratings, OUTPUT_RATINGS_FILE)

if __name__ == "__main__":
    main()
