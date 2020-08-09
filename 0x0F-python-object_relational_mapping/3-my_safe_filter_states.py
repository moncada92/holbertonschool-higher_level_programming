#!/usr/bin/python3
"""
select all states in database
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name = %(name)s ORDER BY id",
                {'name': sys.argv[4]})

    rows = cur.fetchall()
    for row in rows:
        if sys.argv[4] == row[1]:
            print(row)
    cur.close()
    db.close()
