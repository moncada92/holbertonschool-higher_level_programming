#!/usr/bin/env python3
"""
select all states in database
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    count = 1

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states \
                ON states.id = cities.state_id \
                WHERE states.name = %(name)s", {'name': sys.argv[4]})

    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print(col, end="")
            if count < len(rows):
                print(", ", end="")
            count += 1
    print()
    cur.close()
    db.close()
