import sqlite3
from datetime import datetime
import pandas as pd


# -----------------------------
# CREATE DATABASE
# -----------------------------
def create_database():

    conn = sqlite3.connect("data/attendee.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendees(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        email TEXT,

        phone TEXT,

        college TEXT,

        department TEXT,

        event TEXT,

        city TEXT,

        age INTEGER,

        gender TEXT,

        registration_time TEXT,

        checkin_status TEXT,

        checkin_time TEXT

    )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# ADD ATTENDEE
# -----------------------------
def add_attendee(name, email, phone, college,
                 department, event, city,
                 age, gender):

    conn = sqlite3.connect("data/attendee.db")

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO attendees
    (
        name,
        email,
        phone,
        college,
        department,
        event,
        city,
        age,
        gender,
        registration_time,
        checkin_status,
        checkin_time
    )

    VALUES(?,?,?,?,?,?,?,?,?,?,?,?)

    """,

    (
        name,
        email,
        phone,
        college,
        department,
        event,
        city,
        age,
        gender,
        datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Pending",
        ""
    ))

    conn.commit()
    conn.close()


# -----------------------------
# GET ALL ATTENDEES
# -----------------------------
def get_all_attendees():

    conn = sqlite3.connect("data/attendee.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendees")

    rows = cursor.fetchall()

    conn.close()

    return rows


# -----------------------------
# GET DATAFRAME
# -----------------------------
def get_dataframe():

    conn = sqlite3.connect("data/attendee.db")

    df = pd.read_sql_query("SELECT * FROM attendees", conn)

    conn.close()

    return df


# -----------------------------
# CHECK-IN ATTENDEE
# -----------------------------
def checkin_attendee(attendee_id):

    conn = sqlite3.connect("data/attendee.db")

    cursor = conn.cursor()

    cursor.execute("""

    UPDATE attendees

    SET

        checkin_status=?,

        checkin_time=?

    WHERE id=?

    """,

    (

        "Checked In",

        datetime.now().strftime("%d-%m-%Y %H:%M:%S"),

        attendee_id

    ))

    conn.commit()

    conn.close()


# -----------------------------
# CREATE DATABASE ON START
# -----------------------------
create_database()