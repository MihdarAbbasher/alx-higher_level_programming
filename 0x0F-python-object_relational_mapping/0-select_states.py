#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa
 Usage: ./0-select_states.py <mysql username>
  <mysql password> <database name >
  ascending order by state.id
"""

import sys
import MySQLdb

if __name__ == "__main__":
    my_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    quer = my_db.cursor()
    quer.execute("SELECT * FROM `states` ORDER BY states.id")
    [print(state) for state in quer.fetchall()]
