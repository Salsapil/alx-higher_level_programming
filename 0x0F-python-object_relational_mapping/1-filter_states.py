#!/usr/bin/python3
"""lists all states with a name starting with N (upper N)"""
import sys
import MySQLdb

if __name__ == "__main__":

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if (row[1][0] == "N"): {
            print(row)
        }
    cur.close()
    conn.close()
