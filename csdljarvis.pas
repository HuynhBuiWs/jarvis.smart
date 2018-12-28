import sqlite3 as lite
import sys
import os
path = os.path.dirname(__file__) + "\\test.db"
con = lite.connect(path)
 
with con:
     
    cur = con.cursor()    
    cur.execute("CREATE TABLE Cars(hoi INT, traloi TEXT)")