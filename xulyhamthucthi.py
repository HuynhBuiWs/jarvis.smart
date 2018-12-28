#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys
import os
path = os.path.dirname(__file__) + "\\data2.db"
con = lite.connect(path)
 
with con:
    
    cur = con.cursor()    
    cur.execute("DROP TABLE IF EXISTS hamthucthi2")
    cur.execute("CREATE TABLE hamthucthi2(Id TEXT, Name TEXT,Id2 TEXT, Name2 TEXT,Id3 TEXT, Name3 TEXT,Id4 TEXT, Name4 TEXT,Id5 TEXT, Name5 TEXT,Id6 TEXT, Name6 TEXT)")
    cur.execute("INSERT INTO hamthucthi2 VALUES('VỊ TRÍ','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('KHỎE KHÔNG','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('MẤY GIỜ','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('CẢM ƠN','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('MỞ ĐÈN','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('ĐI NGỦ','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('TẮT ĐÈN','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('MỞ MÁY LẠNH','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('TẮT MÁY LẠNH','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('MỞ ĐÈN','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('ĐI NGỦ','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('TÌM','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('PHÁT','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")
    cur.execute("INSERT INTO hamthucthi2 VALUES('TÊN','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa','aaa')")