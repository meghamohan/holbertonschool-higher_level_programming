#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    usr = sys.argv[1]
    pswd = sys.argv[2]
    database = sys.argv[3]
    dbConnection = MySQLdb.connect(host="localhost", port=3306, user=usr, passwd=pswd, db=database)
    crsr = dbConnection.cursor()
    crsr.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    states = crsr.fetchall()
    if states:
        for state in states:
            print(state)
    crsr.close()
    dbConnection.close()
