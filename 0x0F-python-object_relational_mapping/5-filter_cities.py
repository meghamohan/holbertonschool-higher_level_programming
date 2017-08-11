#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
 and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    usr = argv[1]
    pswd = argv[2]
    database = argv[3]
    cityName = argv[4]

    dbConnection = MySQLdb.connect(user=usr, passwd=pswd,
                                   db=database, port=3306,
                                   host="localhost")
    cursr = dbConnection.cursor()
    query = """SELECT cities.name FROM cities
            WHERE state_id IN (SELECT states.id
             FROM states WHERE name = %s);"""
    cursr.execute(query, (cityName,))
    citiess = cursr.fetchall()
    separator = ""
    for city in cities:
        print(separator, end="")
        print(city[0], end="")
        separator = ", "
    print()
    cursr.close()
    dbConnection.close()
