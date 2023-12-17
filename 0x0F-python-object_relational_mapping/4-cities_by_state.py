#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
  <mysql password> <database name >
  ascending order by state.id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `cities` ORDER BY cities.id"
    cur.execute(query)
    [print(state) for state in quer.fetchall() if state[1][0] == "N"]
