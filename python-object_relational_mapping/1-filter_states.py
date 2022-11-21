#!/usr/bin/python3
"""
Writing a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    ''' BINARY performs a byte-by-byte comparison, aside from the
    common character-by-character comparison, which is more
    'acurate' for this case needed '''
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
                   'N%' ORDER BY id ASC;")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
