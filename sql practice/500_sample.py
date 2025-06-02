# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 19:40:35 2024

@author: Dixit
"""
from sqlalchemy import *
# Attempt to rebuild the database and provide a download link again
import random

# Create an SQLite database file 'friends.db'
engine = create_engine('sqlite:///mnt/data/friends.db', echo=False)

# Re-create the metadata and friends table schema
metadata = MetaData()

friends = Table('friends', metadata,
    Column('Friend_ID', Integer, primary_key=True),
    Column('Friend_Name', String),
    Column('Friend_Phone_no', String)
)

metadata.create_all(engine)

# Generate 500 rows of random data (names and phone numbers)
names = ['John Doe', 'Jane Smith', 'Emily Johnson', 'Michael Brown', 'Chris Davis', 'Jessica Wilson', 'David Anderson']
phone_numbers = [f'{random.randint(600, 999)}{random.randint(1000000, 9999999)}' for _ in range(500)]

data = [{'Friend_Name': random.choice(names), 'Friend_Phone_no': random.choice(phone_numbers)} for _ in range(500)]

# Insert data into the 'friends' table
with engine.connect() as connection:
    connection.execute(friends.insert(), data)

# Path to the created database file
db_path = '/mnt/data/friends.db'
db_path
