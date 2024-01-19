import sqlite3

conn = None

try:
    conn = sqlite3.connect("foobar.db")
except (sqlite3.DatabaseError, sqlite3.OperationalError) as err:
    print(err)
    exit(1)
else:
    cursor = conn.cursor()
    # make queries....
finally: # always executed
    if conn is not None:  # clean up resources
        conn.close()
