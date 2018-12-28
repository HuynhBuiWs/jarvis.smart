#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import os
path = os.path.dirname(__file__) + "\\data2.db"
con = lite.connect(path)
 
with con:
    
    cur = con.cursor()    
    cur.execute("CREATE TABLE hoidap(Id TEXT, Name TEXT)")
    cur.execute("INSERT INTO hoidap VALUES('ancom','anchao')")
