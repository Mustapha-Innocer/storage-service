import os

from dotenv import load_dotenv

load_dotenv()

KAFKA_SERVER = os.getenv("KAFKA_SERVER", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
KAFKA_CONSUMER_TOPIC = os.getenv("KAFKA_TOPIC", "processed-data")

DB_URL = os.getenv("DB_URL", "postgresql://username:password@host:port/dbname")
