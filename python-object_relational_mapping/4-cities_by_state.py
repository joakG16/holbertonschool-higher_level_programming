#!/usr/bin/python3
"""
Writing a script that lists all cities joining states by the state id
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities INNER JOIN states ON cities.state_id\
        = states.id ORDER BY cities.id ASC;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
