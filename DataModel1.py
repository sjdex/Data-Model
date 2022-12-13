import psycopg2

def createDB(name):
    try:
        conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=password")
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        cur.execute("DROP DATABASE IF EXISTS "+name)
        cur.execute("CREATE DATABASE "+name)
        print("Database "+name+" created.")
        conn.close()

        conn = psycopg2.connect("host=127.0.0.1 dbname="+name+" user=postgres password=password")
        cur = conn.cursor()

        return cur, conn
    except psycopg2.Error as e:
        print(e)

def createTable(cur, conn, create_query):
    cur.execute(create_query)
    conn.commit()
    print("Table created.")

def insertIntoTable(cur, conn, dfname, insert_query):
    for i, row in dfname.iterrows():
        cur.execute(insert_query, list(row))
    conn.commit()

teams_table_create = ("""CREATE TABLE IF NOT EXISTS teams (
team VARCHAR PRIMARY KEY,
points INT
)""")
players_table_create = ("""CREATE TABLE IF NOT EXISTS players (
nationality VARCHAR,
player_name VARCHAR
)""")

teams_insert = ("""INSERT INTO teams(
team,
points) VALUES (%s, %s)
""")

players_insert = ("""INSERT INTO players(
nationality,
player_name) VALUES (%s, %s)
""")

