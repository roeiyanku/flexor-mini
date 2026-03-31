from app.db import get_connection


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (
        id SERIAL PRIMARY KEY,
        speaker TEXT,
        transcript TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interview_features (
        interview_id INT PRIMARY KEY REFERENCES interviews(id),
        mentions_kitchen BOOLEAN,
        wants_storage BOOLEAN,
        mentions_light BOOLEAN,
        sentiment TEXT,
        summary TEXT
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()


def reset_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("TRUNCATE TABLE interview_features, interviews RESTART IDENTITY CASCADE;")

    conn.commit()
    cursor.close()
    conn.close()


def insert_interview(speaker, transcript):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews (speaker, transcript)
    VALUES (%s, %s)
    RETURNING id;
    """, (speaker, transcript))

    interview_id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()

    return interview_id


def get_all_interviews():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, speaker, transcript FROM interviews;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def insert_features(interview_id, features):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interview_features (
        interview_id,
        mentions_kitchen,
        wants_storage,
        mentions_light,
        sentiment,
        summary
    )
    VALUES (%s, %s, %s, %s, %s, %s);
    """, (
        interview_id,
        features["mentions_kitchen"],
        features["wants_storage"],
        features["mentions_light"],
        features["sentiment"],
        features["summary"]
    ))

    conn.commit()
    cursor.close()
    conn.close()


def get_all_features():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM interview_features;")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows