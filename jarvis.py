#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
# -*- coding: utf-8 -*-
import speech_recognition as sr
from time import ctime, strftime
import time
import sqlite3 as lite
import os
from gtts import gTTS
import sys
import webbrowser
import json
import requests
import random
import urllib.request
import urllib.parse
import re
import wave



from pygame import mixer
#ket noi voi csdl
path = os.path.dirname(__file__) + "\\data2.db"
con = lite.connect(path)
#khoi dong bo phat
mixer.init()
#ham tu them vao csdl

def themdata(ques,ans):
    dulieu=(ques,ans)
    with con:
        cur=con.cursor()

        cur.execute("INSERT INTO hamthucthi VALUES(?,?)",dulieu)
def hamcat(data):
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM hamcat")
        rows=cur.fetchall()
        for row in rows:
            for i in range(0,1):
                if row[i] in data:
                    data=data.replace(str(row[i]),"")
                    print(data)
    return data
def truyxuat(data):
    
    with con:
    
        cur = con.cursor()    
    
        cur.execute("SELECT * FROM hoidap")
    
        rows=cur.fetchall()
        
        for row in rows:
            if row[0] in data:
                
                
                
                speak(row[0]+ " CÓ NGHĨA LÀ " + row[1])



def dieukhien(domain,action,entity):

 

    url = 'https://.duckdns.org/api/services/' + domain + '/turn_'+ action + '?api_password='
    payload = {'entity_id': entity}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(payload), headers=headers)
def speak(audioString):
    url = 'http://api.openfpt.vn/text2speech/v4'
    headers = {'api_key': '7121c9185cf9404595f297f23d352039','speed':'1','prosody':'1', 'voice':'female'}
    
    payload = str(audioString).encode('utf-8')
    print(payload)

    r = requests.post(url, data=payload, headers=headers)
    datajson = r.json()
    datajson=datajson['async']
    print(datajson)
    time.sleep(1)
    urltts = datajson
  
    r = requests.get(urltts)

    with open('audio.mp3', 'wb') as f:  
        f.write(r.content)
    
    
    print(audioString)
    mixer.quit()
    mixer.init(48000, -16, 2, 4096)

    print(mixer.get_init())


    mixer.music.load('audio.mp3')
    mixer.music.play()
    os.remove('audio.mp3')

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
 
    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio,language='vi-VN')
        
    except sr.UnknownValueError:
        print("sao đại ca không nói gì")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data

def traloi(ans1,ans2,ans3):

        caunoi=[ans1,ans2,ans3]
        
        speak(random.choice(caunoi))
        time.sleep(2)

def hamthucthi(row0,data):
    if row0== "KHỎE KHÔNG":
        print(data)
        traloi("em khỏe","khỏe lắm ạ","khỏe chứ đại ca")               
    if row0== "CẢM ƠN":
        traloi('không có chi','rất vui ạ','đừng bận tâm ạ')
    if row0=="MẤY GIỜ":
        
        speak("BÂY GIỜ LÀ " + strftime("%H:%M") + " PHÚT " + "ĐÓ ĐẠI CA")
        time.sleep(5)
    if row0=="VỊ TRÍ":
        if "CỦA" in data:
            locationcua = data.find('CỦA')
            data = data[locationcua+4:len(data)]
            location = data.strip(" ")
            speak("đây là vị trí của  " + location )
            webbrowser.open("https://www.google.nl/maps/place/" + location + "/&amp;")
            time.sleep(5)
    if row0=="MỞ ĐÈN":
        dieukhien('switch','on','switch.main_light_1')
        dieukhien('switch','on','switch.main_light_2')
        traloi('ok đại ca','đã mở đèn cho đại ca','đèn đã mở' )
        
    if row0=="ĐI NGỦ":
        dieukhien('script','on','script.go_to_sleep')
    if row0=="TẮT ĐÈN": 
        dieukhien('switch','off','switch.main_light_1')
        dieukhien('switch','off','switch.main_light_2')
        traloi('ok đại ca','đã tắt đèn cho đại ca','đèn đã tắt' )
    if row0=="MỞ MÁY LẠNH":
        dieukhien('switch','on','switch.air_conditioner')
        traloi('ok đại ca','đã mở máy lạnh cho đại ca','máy lạnh đã mở ')

    if row0=="TẮT MÁY LẠNH":
        dieukhien('switch','off','switch.air_conditioner')
        traloi('ok đại ca','đã tắt máy lạnh cho đại ca','máy lạnh đã tắt')     
    if row0=="TÌM":
        if "GOOGLE" in data:
            locationtim=data.find('TÌM')
            data=data[locationtim+4:len(data)]
            locationgugo=data.find('GOOGLE')
            data=data[0:locationgugo-5]
            webbrowser.open('https://www.google.co.in/#q='+data)
            traloi('OK ĐẠI CA','KẾT QUẢ ĐÂY ĐẠI CA','CÓ NGAY ĐẠI CA')

    if row0=="TÌM":
        if "YOUTUBE" in data:
            locationtim=data.find('TÌM')
            data=data[locationtim+4:len(data)]
            locationgugo=data.find('YOUTUBE')
            data=data[0:locationgugo-5]
            webbrowser.open('https://www.youtube.com/results?search_query='+data)
            traloi('OK ĐẠI CA','KẾT QUẢ ĐÂY ĐẠI CA','CÓ NGAY ĐẠI CA')
    if row0=="TÌM":
        if "NHẠC CỦA TUI" in data:
            locationtim=data.find('TÌM')
            data=data[locationtim+4:len(data)]
            locationgugo=data.find('NHẠC CỦA TUI')
            data=data[0:locationgugo-5]
            webbrowser.open('https://www.nhaccuatui.com/tim-kiem?q='+data)
            traloi('OK ĐẠI CA','KẾT QUẢ ĐÂY ĐẠI CA','CÓ NGAY ĐẠI CA')

    if row0=="PHÁT" :
 
        if "YOUTUBE" in data:
            locationtim=data.find('PHÁT')
            data=data[locationtim+5:len(data)]
            locationgugo=data.find('YOUTUBE')
            data=data[0:locationgugo-5]
            query_string = urllib.parse.urlencode({"search_query" : data})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            webbrowser.open("http://www.youtube.com/watch?v=" + search_results[random.randint(0,10)])
            time.sleep(5)

    if row0=="MỞ":
        if "CAMERA" in data:
            traloi('OK ĐẠI CA','ĐÂY ĐẠI CA','CÓ NGAY ĐẠI CA')
            webbrowser.open("http://192.168.9.103:8081")
    if row0=="TÊN":
        if "EM" in data: 
            traloi('em là lb minh nha đại ca','em là lb minh nha đại ca','em là lb minh nha đại ca',)
    if "CÓ NGHĨA LÀ" in data:
        if "KHI ANH NÓI" in data:
            data = data.replace("KHI ANH NÓI","")
            ques=data[1:data.find("CÓ NGHĨA LÀ")-1]
            ans=data[data.find("CÓ NGHĨA LÀ")+12:len(data)]
            themdata(ques,ans)
            traloi("NHỚ RỒI ĐẠI CA","ĐÃ HỌC XONG ĐẠI CA","CÁM ƠN ĐẠI CA")
def timkiemthucthi(data):
    with con:
        cur=con.cursor()
        cur.execute("SELECT * FROM hamthucthi2")
        rows=cur.fetchall()
        for row in rows:
            b=0
            
            for i in range(0,11):
                if row[i] in data:
                    hamthucthi(row[0],data)
                    b=1
                    break
                
            if b==1:
                break
def jarvis(data):
    data=data.upper()
    print(data)
    
    hamcat(data)
    timkiemthucthi(data)
        



    


    
    
# initialization

time.sleep(2)
traloi('đại ca muốn hỏi gì','đại ca hỏi gì đi','chào đại ca')

while 1:
    data = recordAudio()
    jarvis(data)
