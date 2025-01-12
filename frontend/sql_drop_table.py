import sqlite3
import os


main_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(main_path)

dbname = "sales_info.db"
conn = sqlite3.connect(dbname)
c = conn.cursor()

query = "DROP TABLE IF EXISTS users"
c.execute(query)
conn.commit()
conn.close()