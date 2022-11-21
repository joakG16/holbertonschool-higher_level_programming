#!/usr/bin/python3
"""
Making a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
Basically make a subquery, for finding the state's id through user input
state's name, and then with the id, compare it to the city's state id to
collect the desired cities, in the main query.
HAS TO BE SQL INJECTION-FREE!
"""
import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cursor = conn.cursor()
    query_and_subqu = ("SELECT cities.name FROM cities WHERE cities.state_id =\
         (SELECT states.id FROM states WHERE states.name = %s)\
            ORDER BY cities.id ASC;")
    cursor.execute(query_and_subqu, (sys.argv[4], ))
    query_rows_tuple = cursor.fetchall()  # fetchall() returns a tuple, 
    cities = [tup_elem[0] for tup_elem in query_rows_tuple]  # l. comprehension
    for city in cities:
        if city == cities[-1]:  # last element in list with newline
            print(city)
        else:
            print(city, end=", ")
    cursor.close()
    conn.close()
