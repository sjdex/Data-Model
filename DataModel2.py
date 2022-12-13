import pandas as pd
import DataModel1

try:
    #Creating DataFrames
    teams = pd.read_csv("Data/Teams.csv")
    teams = teams.drop(['Image'], axis=1)

    players = pd.read_csv("Data/Players.csv", encoding='ISO-8859-1')

    #Create Database
    cur, conn = DataModel1.createDB("worldcup")

    #Create Tables
    DataModel1.createTable(cur, conn, DataModel1.teams_table_create)
    DataModel1.createTable(cur, conn, DataModel1.players_table_create)

    #Insert data from csv file to tables
    DataModel1.insertIntoTable(cur, conn, teams, DataModel1.teams_insert)
    DataModel1.insertIntoTable(cur, conn, players, DataModel1.players_insert)
finally:
    cur.close()
    conn.close()