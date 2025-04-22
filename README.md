# 🗄️ Storage Service - News Aggregator Backend

The Storage Service is a microservice responsible for persisting enriched news stories (summarized and categorized) into a relational database. It consumes structured news data from Kafka and stores it in normalized tables including related entities like sources, authors, and categories.

---

## 🛠 Features

- ✅ Stores processed news articles in a relational DB
- 📌 Normalized schema with:
  - `stories` table
  - `sources`, `authors`, `categories` as separate related tables
- 🧵 Consumes Kafka topic with summarized & classified news
- ⚙️ SQLAlchemy ORM for DB interactions
- 🐘 Uses PostgreSQL
- 📦 Dockerized for production use
- 🔁 CI with GitHub Actions

---

## 🧱 Tech Stack

- **Python** 3.13
- **Kafka** (consumer)
- **PostgreSQL**
- **SQLAlchemy** + Alembic for migrations
- **Docker**
- **GitHub Actions** for CI

---

## 🧬 Database Schema Overview

coming soon!

---

## 🔧 Environment Variables

```env
# Kafka
KAFKA_SERVER=localhost
KAFKA_PORT=9094

# PostgreSQL
DB_URL=DB_URL=postgresql://username:password@host:port/dbname
```

---

## 🚀 Getting Started

1. Clone the repo

2. Create and populate your `.env` file

3. Create new python virtual environment

```bash
python -m venv venv
```

4. Intall the python dependencies

```bash
pip install -r requirements.txt
```

5. Run migrations

```bash
alembic upgrade head
```

6. Run

```bash
python main.py
```

---

## 🧱 Related Services

This is part of a larger microservice-based system. See the [Main Project README](https://github.com/Mustapha-Innocer/news-aggregator) for architecture and links to all services.
