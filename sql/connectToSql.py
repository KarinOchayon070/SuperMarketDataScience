import sqlite3
from tablesConfig import categoriesToEnter, supersToEnter, itemsToEnter


conn = sqlite3.connect('crawlerData.db')


# This creates the tables needed
conn.execute(
    'CREATE TABLE IF NOT EXISTS SuperMarkets (super_id INTEGER PRIMARY KEY, super_name TEXT)')

conn.execute(
    'CREATE TABLE IF NOT EXISTS Category (category_id INTEGER PRIMARY KEY, category_name TEXT)')


# for super in supersToEnter:
#     conn.execute(
#         f"INSERT OR IGNORE INTO SuperMarkets (super_name) VALUES ('{super}')")

# for category in categoriesToEnter:
#     conn.execute(
#         f"INSERT OR IGNORE INTO Category (category_name) VALUES ('{category}')")


cur = conn.cursor()

# cur.execute("SELECT * FROM SuperMarkets")

rows = cur.fetchall()

# print(rows)


conn.commit()
conn.close()
