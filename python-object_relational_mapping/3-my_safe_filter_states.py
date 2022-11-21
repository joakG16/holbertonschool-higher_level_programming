#!/usr/bin/python3
"""
Like Task 2, write a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa where name matches the
argument. But this time, write one that is safe from MySQL injections!

Important: SQL injection is a code injection technique used to attack
data-driven applications, in which malicious SQL statements are inserted
into an entry field for execution (e.g. to dump the database contents
to the attacker)
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    query_txt = "SELECT * FROM states WHERE name LIKE BINARY\
    %s ORDER BY id ASC;"  # parametized query
    cursor.execute(query_txt, (sys.argv[4], ))  # the input in the tuple
    # will supply the previous query in a safe way, being automatically quoted
    # staying as a string and preventing therefore to be malicious user input
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    conn.close()
