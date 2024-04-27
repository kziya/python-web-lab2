import os

import psycopg

connection = psycopg.connect(user=os.getenv("DB_USER"),
                             password=os.getenv("DB_PASSWORD"),
                             host=os.getenv('DB_HOST'),
                             port=os.getenv('DB_PORT'),
                             dbname=os.getenv('DB_NAME')
                             )


# Create tables


def get_db():
    return connection.cursor()
