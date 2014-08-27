"""
------------------------------------
File name: TransData.py
Date: 10/14/2013
Programmer: Zhijiao Liu
UIN: 522-00-4372
Email: zhijiao.liu.imp@gmail.com
MySQL software: MySQL Workbench 6.0
Python 2.7.5
------------------------------------
"""


import csv
import pymysql

pymysql.install_as_MySQLdb()

#built connection with the database
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='')
cur = conn.cursor()

#show all the databases that can be used
cur.execute("show databases")
for r in cur.fetchall():
   print(r)

print "----------------------"

#use NBA database and show its tables
cur.execute("use NBA")

cur.execute("show tables")
for r in cur.fetchall():
   print(r)

#can directly drop database in this Python program
#cur.execute("drop NBA")
"""
#insert the data of table Schedule
with open('Schedule.txt', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
        datetimeStr = row[2] + " " + row[3]
#       print datetimeStr
        cur.execute("INSERT INTO Schedule(Home, Away, Time, Place) VALUES (%s,%s,%s, %s)",(row[0],row[1],datetimeStr,row[4]))
conn.commit()

#insert the data of table Coaches
with open('Coaches.txt', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
#        print row[0]
        cur.execute("INSERT INTO Coaches(Name, Team, Position) VALUES (%s,%s,%s)",(row[0],row[1],row[2]))
conn.commit()
"""
#insert the data of table Players
with open('Players.txt', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
#        print row[0]
        cur.execute("INSERT INTO Players(Name, Number, Team, Position, Hight, Weight, DoB, Years, Country, PriorToNBA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9]))
conn.commit()
"""
#insert the data of table Teams
with open('Teams.txt', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
#        print row[0],row[1],row[2],row[3],row[4],row[5],row[6]
        cur.execute("INSERT INTO Teams(TeamName, City, State, Conference, Division, MainCourt, ChampionshipNum) VALUES (%s, %s, %s, %s, %s, %s, %s)",(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
conn.commit()

#insert the data of table Contracts
with open('Contracts.txt', 'rU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar=',')
    for row in spamreader:
#        print row[0],row[1],row[2],row[3]
        cur.execute("INSERT INTO Contracts(Player,Team,Salary,End) VALUES (%s, %s, %s, %s)",(row[0],row[1],row[2],row[3]))
conn.commit()
"""

#Disconnection
cur.close()
conn.close()
