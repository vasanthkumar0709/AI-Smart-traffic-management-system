import sqlite3


def create_database():

    connection = sqlite3.connect("traffic.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS traffic_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            total INTEGER,
            cars INTEGER,
            bikes INTEGER,
            buses INTEGER,
            trucks INTEGER,
            density TEXT,
            green_time INTEGER
        )
    """)

    connection.commit()
    connection.close()


def insert_data(
    total,
    cars,
    bikes,
    buses,
    trucks,
    density,
    green_time
):

    connection = sqlite3.connect("traffic.db")

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO traffic_data
        (
            total,
            cars,
            bikes,
            buses,
            trucks,
            density,
            green_time
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        total,
        cars,
        bikes,
        buses,
        trucks,
        density,
        green_time
    ))

    connection.commit()
    connection.close()