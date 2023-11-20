#!/usr/bin/python3

"""
    Module to lists all states with a name starting with N
"""

if __name__ == "__main__":
    import MySQLdb
    import sys


    def list_states_starting_with_n(username, password, database):
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        states = cursor.fetchall()
        for state in states:
            print(state)

        cursor.close()
        db.close()

    if len(sys.argv) != 4:
        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    list_states_starting_with_n(username, password, database)
