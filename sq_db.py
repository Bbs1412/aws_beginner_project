# Sqlite code to create the db and all:

import os
import json
import sqlite3
from datetime import datetime

# -------------------------------------------------------------------------------------
# Database:
# -------------------------------------------------------------------------------------

# Clear entire database:
def clear_db():
    # backup the db into db_backup folder:
    if not os.path.exists('db_backup'):
        os.mkdir('db_backup')

    os.system(
        f'copy lite.db db_backup\lite{datetime.now().strftime("_%Y-%m-%d_%H-%M")}.db')

    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        DROP TABLE IF EXISTS LOCATIONS
        """
    )
    cur.execute(
        """
        DROP TABLE IF EXISTS MAPS
        """
    )
    cur.execute(
        """
        DROP TABLE IF EXISTS LOCATION_DETAILS
        """
    )
    conn.commit()
    conn.close()


# -------------------------------------------------------------------------------------
# Tables Management:
# -------------------------------------------------------------------------------------

# Create the Locations table to hold the basic data:
def create_locations():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LOCATIONS (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            image TEXT, image2 TEXT,
            image3 TEXT, image4 TEXT
        )
        """
    )
    conn.commit()
    conn.close()


# Create the Maps table to hold the map data for the location:
def create_maps():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS MAPS (
            id INTEGER PRIMARY KEY,
            location_id INTEGER,
            map_iframe TEXT,
            latitude REAL,
            longitude REAL,
            FOREIGN KEY (location_id) REFERENCES LOCATIONS(id)
        )
        """
    )
    conn.commit()
    conn.close()


# Details table to hold the details of the location for web page:
def create_location_details():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS LOCATION_DETAILS (
            id INTEGER PRIMARY KEY,
            location_id INTEGER,
            description_intro TEXT,
            description_history TEXT,
            description_highlights TEXT,
            description_tips TEXT,
            FOREIGN KEY (location_id) REFERENCES LOCATIONS(id)
        )
        """
    )
    conn.commit()
    conn.close()


# -------------------------------------------------------------------------------------
# Data Operations:
# -------------------------------------------------------------------------------------

# Fn to insert data into Locations table:
def insert_location(id, name, location, image, image2, image3, image4):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO LOCATIONS (id, name, location, image, image2, image3, image4)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (id, name, location, image, image2, image3, image4)
    )
    conn.commit()
    conn.close()


# Fn to insert data into Maps table:
def insert_map(location_id, map_iframe, latitude, longitude):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO MAPS (location_id, map_iframe, latitude, longitude)
        VALUES (?, ?, ?, ?)
        """,
        (location_id, map_iframe, latitude, longitude)
    )
    conn.commit()
    conn.close()


# Fn to insert data into Location Details table:
def insert_location_details(location_id, description_intro, description_history, description_highlights, description_tips):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO LOCATION_DETAILS (location_id, description_intro, description_history, description_highlights, description_tips)
        VALUES (?, ?, ?, ?, ?)
        """,
        (location_id, description_intro, description_history,
         description_highlights, description_tips)
    )
    conn.commit()
    conn.close()

# -------------------------------------------------------------------------------------
# Helper Functions:
# -------------------------------------------------------------------------------------

def get_iframe_code(src, width=350, height=300):
    defaults_just_saved = '''
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d14994.081656486365!2d75.15761048715821!3d20.02863330000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bdb92609201a9eb%3A0xe0639ba6286a474!2sEllora%20Cave%20No.%2029%20The%20Dhumar%20Lena!5e0!3m2!1sen!2sin!4v1731098951522!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" 
        referrerpolicy="no-referrer-when-downgrade"></iframe>
    '''

    return f'<iframe src="{src}" width="{width}" height="{height}" style="border:0; border-radius:10px; opacity:1.0; filter: invert(1.0);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>'


# -------------------------------------------------------------------------------------
# Functions to call from server:
# -------------------------------------------------------------------------------------

# Fn to call from server which returns location based on id (for specific location page):
def get_location_data(id, output_format='json'):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM LOCATIONS WHERE id = ?
        """,
        (id,)
    )
    location = cur.fetchone()
    headers = [description[0] for description in cur.description]
    conn.close()

    resp = {}
    if location:
        resp = dict(zip(headers, location))

    if output_format == 'dict':
        return resp
    else:
        return json.dumps(resp, indent=5)


# Get map data of location based on location_id:
def get_map_data(location_id, output_format='json'):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM MAPS WHERE location_id = ?
        """,
        (location_id,)
    )
    location_map = cur.fetchone()
    headers = [description[0] for description in cur.description]
    conn.close()

    resp = {}
    if location_map:
        resp = dict(zip(headers, location_map))

    if output_format == 'json':
        return json.dumps(resp, indent=5)
    else:
        return resp


# Get all locations: (meant to be called from the client side js)
def get_all_locations_data(output_format='json'):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        SELECT * FROM LOCATIONS
        """
    )
    locations = cur.fetchall()
    headers = [description[0] for description in cur.description]
    conn.close()
    locations_list = []

    for location in locations:
        location_dict = dict(zip(headers, location))
        locations_list.append(location_dict)

    if output_format == 'json':
        return json.dumps(locations_list, indent=5)
    else:
        return locations_list


# Get location details (text data) to render the page for a specific location:
def get_place_details(place_id, output_format='json'):
    # only return location_id, description_intro, description_history, description_highlights, description_tips (json format by default):
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute(
        """
        SELECT location_id, description_intro, description_history, description_highlights, description_tips
        FROM LOCATION_DETAILS
        WHERE location_id = ?
        """,
        (place_id,)
    )
    location_details = cur.fetchone()
    headers = [description[0] for description in cur.description]
    conn.close()

    resp = {}
    if location_details:
        resp = dict(zip(headers, location_details))

    if output_format == 'json':
        return json.dumps(resp, indent=5)
    else:
        return resp
