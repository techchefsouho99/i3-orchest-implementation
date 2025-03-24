import os
import pandas as pd
from kafka import KafkaConsumer
from tqdm import tqdm

# Kafka Configuration
KAFKA_SERVER = 'localhost:9092'
TOPIC = 'movielog16'

def main():
    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
    )

    print(f"Connected to Kafka topic: {TOPIC}")

    watch_history = []
    ratings = []
    recommendation_requests = []

    print("Reading messages from Kafka...")
    for message in tqdm(consumer):
        message = message.value.decode()

        # Extract timestamp and user_id
        parts = message.split(",")
        if len(parts) < 3:
            continue  # Skip malformed logs

        timestamp, user_id, action = parts[:3]

        # Recommendation request event
        if "recommendation request" in action:
            rec_result = action.split("result: ")[-1]
            recommendation_requests.append((timestamp, user_id, rec_result))

        # Movie watch history event
        elif "GET /data/m/" in action:
            movie_id = action.split("/")[3]
            watch_history.append((timestamp, user_id, movie_id))

        # Rating event
        elif "GET /rate/" in action:
            rating_info = action.split("=")
            if len(rating_info) == 2:
                movie_id, rating = rating_info[0].split("/")[-1], rating_info[1]
                ratings.append((timestamp, user_id, movie_id, int(rating)))

            # Optional: log raw Kafka message
            os.system(f"echo {message} >> kafka_ratings_log.csv")

        # Milestone 1: limit to 10000 ratings
        if len(ratings) > 10000:
            break

    # Summary
    print(f"\nParsing complete:")
    print(f"  Ratings collected: {len(ratings)}")
    print(f"  Watch history entries: {len(watch_history)}")
    print(f"  Recommendation requests: {len(recommendation_requests)}")

if __name__ == "__main__":
    main()
