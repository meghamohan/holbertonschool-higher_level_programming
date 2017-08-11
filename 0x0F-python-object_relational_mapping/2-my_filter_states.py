#!/usr/bin/python3
"""
script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa
 where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    usr = argv[1]
    pswd = argv[2]
    database = argv[3]
    stateNme = argv[4]

    dbConnection = MySQLdb.connect(user=usr, passwd=pswd,
                                   db=database, port=3306,
                                   host="localhost")
    cursr = dbConnection.cursor()
    cursr.execute("SELECT * FROM states WHERE BINARY name"
                  "='{:s}' ORDER BY states.id ASC".format(stateNme))
    states = cursr.fetchall()
    for state in states:
        print(state)
    cursr.close()
    dbConnection.close()
