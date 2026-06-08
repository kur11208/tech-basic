import sqlite3


# Connect to etf_app.db
connection = sqlite3.connect("etf_app.db")

# Close the connection
connection.close()
