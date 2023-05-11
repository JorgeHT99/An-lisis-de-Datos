import pandas as pd 
import sqlite3
path = '../../'
database = path + 'database.sqlite'
# iniciar coneccion con la base de datos
conn = sqlite3.connect(database)
# estructura 'global' de la base de datos
tables = pd.read_sql("""SELECT * FROM sqlite_master
                        WHERE type='table';""", conn)
tables

league = pd.read_sql("""SELECT *
                        FROM League;""", conn)
league