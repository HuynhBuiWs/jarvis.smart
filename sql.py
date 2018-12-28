#!usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import os
import time
 




con = lite.connect('test.db')

with con:
    
    cur = con.cursor()    
    
    cur.execute("SELECT * FROM Cars")
    
    rows=cur.fetchall()
    time.sleep(1)
    for row in rows:
    	if (row[0]) == 4:
    		print(row[1], row[2])
