#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import os
path = os.path.dirname(__file__) + "\\data2.db"
con = lite.connect(path)
 
with con:
    
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS hamcat")
    cur.execute("CREATE TABLE hamcat(Id TEXT, Name TEXT)")
    cur.execute("INSERT INTO hamcat VALUES('NÓI CHO ANH NGHE','NÓI CHO ANH')")
    cur.execute("INSERT INTO hamcat VALUES('NÓI CHO ANH BIẾT','NÓI ANH BIẾT')")
    cur.execute("INSERT INTO hamcat VALUES('NÓI CHO TAO NGHE','NÓI CHO TAO')")
    cur.execute("INSERT INTO hamcat VALUES('NÓI CHO TAO BIẾT','NÓI TAO BIẾT')")