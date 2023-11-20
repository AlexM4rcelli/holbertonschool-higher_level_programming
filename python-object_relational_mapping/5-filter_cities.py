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

        query = """
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id;
                """
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        if cities:
            result = ', '.join(city[0] for city in cities)
            print(result)

        cursor.close()
        db.close()

    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities_by_state(username, password, database, state_name)
