#!/usr/bin/python3
"""
    Module that takes in the name of a state as an argument 
    and lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    import sys


    def list_cities_by_state(username, password, database, state_name):
        db = MySQLdb.connect(host="localhost", port=3306,
                             user=username, passwd=password, db=database)
        cursor = db.cursor()

        query = "SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        cities = cursor.fetchall()
        for city in cities:
            print(city)

        cursor.close()
        db.close()

    if len(sys.argv) != 5:
        print("Usage: mysql <username> <password> <database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
