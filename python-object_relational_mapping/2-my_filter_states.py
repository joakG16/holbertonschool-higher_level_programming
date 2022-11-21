#!/usr/bin/python3
"""
Making a script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where 'name' column matches the argument.
important: use format() method to create the SQL query with user input
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    query_txt = "SELECT * FROM states WHERE name LIKE BINARY\
    '{}' ORDER BY id ASC;".format(sys.argv[4])  # using in example: 'Arizona'
    cursor.execute(query_txt)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
