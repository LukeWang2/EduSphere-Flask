import os, re
import psycopg

URL = "https://storage.googleapis.com/edusphere/low_poly/"

# read the pg connection string from the environment variable
pg_conn_string = os.environ["DATABASE_URL"]
# Get the file names
items = []  # os.listdir("$PATH")

# Connect to an existing database
conn = psycopg.connect(pg_conn_string)
# Open a cursor to perform database operations
cur = conn.cursor()


def make_db():
    # Create seqential ids
    cur.execute("""DROP TABLE models_3d""")
    cur.execute("""DROP SEQUENCE ids""")
    cur.execute(
        """
        CREATE SEQUENCE ids MINVALUE 0 START 0 INCREMENT 1
        """
    )
    # cur.execute("""DROP TABLE models_3d""")
    # Execute a command: this creates a new table
    cur.execute(
        """
        CREATE TABLE models_3d (
            id int DEFAULT nextval('ids'),
            item STRING,
            url STRING)
        """
    )

    # Put all items into database
    for urls in items:
        item_url = URL + urls
        item = re.sub(r"\d+", "", urls[:-9].replace("_", " "))

        cur.execute(
            "INSERT INTO models_3d (item, url) VALUES (%s, %s)",
            (item.lower().strip(), item_url),
        )

        # Make the changes to the database persistent
    conn.commit()


def get_item_by_id(id_num):
    return cur.execute(f"""SELECT * FROM models_3d WHERE id = {id_num} """).fetchone()


# def get_item(item):
#     return cur.execute(f"""SELECT * from models_3d WHERE item = {item}""").fetchone()
