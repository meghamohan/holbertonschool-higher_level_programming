#!/usr/bin/python3
"""
this script lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb
if __name__ == "__main__":
    if len(sys.argv) == 4:
        usr = sys.argv[1]
        pswd = sys.argv[2]
        database = sys.argv[3]
        dbConnection = MySQLdb.connect(host="localhost", port=3306,
                                       user=usr, passwd=pswd, db=database)
        cursr = dbConnection.cursor()
        cursr.execute("SELECT * FROM states")
        states = cursr.fetchall()
        for state in states:
            print(state)
        cursr.close()
        dbConnection.close()
