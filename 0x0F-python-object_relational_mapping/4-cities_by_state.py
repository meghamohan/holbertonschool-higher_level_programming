#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    usr = argv[1]
    pswd = argv[2]
    database = argv[3]

    dbConnection = MySQLdb.connect(user=usr, passwd=pswd,
                                   db=database, port=3306,
                                   host="localhost")
    cursr = dbConnection.cursor()
    query = """SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON state_id WHERE cities.state_id = states.id
        ORDER BY cities.id ASC;"""
    cursr.execute(query)
    states = cursr.fetchall()
    for state in states:
        print(state)
    cursr.close()
    dbConnection.close()
