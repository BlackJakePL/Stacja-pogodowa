
import serial
import json
import mysql.connector
from datetime import datetime

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flush()
mydb = mysql.connector.connect(
    host="localhost", user="phpmyadmin  ", password="qwerty", database="weather"
)

mycursor = mydb.cursor()

sql = "INSERT INTO `data`(`wilgotnosc`, `cisnienie`, `rwysokosc`, `wysokosc`, `temp`, `timestamp`) VALUES(%s,%s,%s,%s,%s,%s);"
while True:
    if ser.in_waiting > 0:

        line = ser.readline().decode("utf-8").strip()
        tmp = line.split("/")
        now = datetime.now()
        dt_object = now.strftime("%m/%d/%Y, %H:%M:%S")
        # 0,1,2,3,4
        temperature = float(tmp[0])
        humidity = float(tmp[1])
        presure = float(tmp[2])
        height = float(tmp[3])
        realHeight = float(tmp[4])

        jsonFile = {
        "temp" : temperature,
        "wilgotnosc" : humidity,
        "cisnienie" : presure,
        "wysokosc" : height,
        "rwysokosc" : realHeight,
        "timestamp" : dt_object
        }
        val = (humidity, presure, realHeight, height, temperature, dt_object)
        mycursor.execute(sql, val)

        mydb.commit()

        with open("data_file.json", "w") as write_file:
            json.dump(jsonFile, write_file)
        print("Collecting data...")
        print(temperature)
        print(presure)
        print(realHeight)
        print(humidity)







^G Get Help      ^O Write Out     ^W Where Is      ^K Cut Text      ^J Justify       ^C Cur Pos       ^Y Prev Page     M-\ First Line   M-W WhereIs Next ^^ Mark Text     M-} Indent Text  M-U Undo         ^B Back
^X Exit          ^R Read File     ^\ Replace       ^U Uncut Text    ^T To Linter     ^_ Go To Line    ^V Next Page     M-/ Last Line    M-] To Bracket   M-^ Copy Text    M-{ Unindent TextM-E Redo         ^F Forward
