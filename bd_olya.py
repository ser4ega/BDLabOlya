import sqlite3 

conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

print('hello') 
conn.execute('PRAGMA foreign_keys = ON') 


c.execute(""" 
CREATE TABLE IF NOT EXISTS USER ( 
Id INTEGER PRIMARY KEY, 
Name TEXT, 
Hash TEXT 
); 

""") 

c.execute(""" 
CREATE TABLE IF NOT EXISTS COMPUTER ( 
Comp_SSID INTEGER PRIMARY KEY, 
Comp_name TEXT, 
Id_user INTEGER, 
Type TEXT, 
CHECK( 
Type = "Ноутбук" OR 
Type = "Стационарный" OR 
Type = "Сервер" 
), 

FOREIGN KEY (Id_user) REFERENCES 
USER(Id) ON DELETE CASCADE 
); 

""") 


c.execute(""" 
CREATE TABLE IF NOT EXISTS USAGE ( 
Date_time DATETIME, 
Prog_name TEXT, 
SSID TEXT, 
Work_time INTEGER, 
CHECK( 
Work_time > 0 
), 
FOREIGN KEY (SSID) REFERENCES COMPUTER(Comp_SSID) ON DELETE RESTRICT 
); 

""") 




conn.commit() 
conn.close()