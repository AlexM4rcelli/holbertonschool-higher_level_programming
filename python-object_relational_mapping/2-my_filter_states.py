#!/usr/bin/python3
"""
    Module to display all values in the states table of hbtn_0e_0_usa 
    where name matches the argument
"""

if __name__ == "__main__":

    import MySQLdb
    import sys


    def search_states(username, password, database, state_name):
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = f"SELECT * FROM states WHERE name = '{state_name}' ORDER BY id ASC"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()

    if len(sys.argv) != 5:
        print("Usage: mysql <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    search_states(username, password, database, state_name)
