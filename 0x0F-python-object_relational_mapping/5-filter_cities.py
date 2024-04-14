#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities of that state"""
import sys
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities \
        join states on cities.state_id = states.id \
            WHERE states.name = '{}' ORDER BY cities.id ASC".format(sys.argv[4]))
    query_rows = cur.fetchall()
    print(", ".join([row[0] for row in query_rows]))
    cur.close()
    conn.close()
