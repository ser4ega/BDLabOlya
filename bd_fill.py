import sqlite3 
import random 
import datetime 
#import sys 
from faker import Faker # для фэйковых дат 
fake =Faker()
conn = sqlite3.connect('Lab3.db') 
c = conn.cursor() 

conn.execute('PRAGMA foreign_keys = ON') 


Names = [ 
'Ольга', 'Юлия', 'Сергей', 'Савелий' 
] 
Comp_names = [ 
'ASUS', 'SF3', 'DSG3H', 'FGBH5', 'F5345GGHF', 'ASDW456' 
] 
# Comp_SSIDs = [ 
# 'Гостиная', 'Зал', 'Кухня', 'Прихожая', 'Спальня' 
# ] 
Types = [ 
'Ноутбук', 'Стационарный', 'Сервер' 

] 
Prog_names=[ 
'Word', 'Excel', 'Explorer', 'Google' 
] 

c.execute("""SELECT *
FROM USER
ORDER BY id DESC
LIMIT 1""")
result =c.fetchall()
if (len(result)>0):
    start_id=result[0][0]+1
else:
    start_id=0
for i in range(start_id,start_id+10): 
    id = i 
    c.execute('INSERT INTO USER (Id, Name, Hash) VALUES (?, ?, ?)', 
    ( 
    id, 
    random.choice(Names), 
    str(hash(random.randint(1, 1000000))) 
    ) 
    ) 

# сохраним занятые ssid в множество
SSIDs=set()
query="SELECT * FROM COMPUTER"
result=c.execute(query).fetchall()
if(len(result)>0):
    for i in range(len(result)):
        SSIDs.add(result[i][0])

for i in range(10): 
    cur_Comp_SSID=random.randint(100,999)
    while(cur_Comp_SSID in SSIDs):
        cur_Comp_SSID=random.randint(100,999)
    SSIDs.add(cur_Comp_SSID)
    query="""INSERT INTO COMPUTER(         
    Comp_SSID , 
    Comp_name , 
    Id_user , 
    Type
    ) VALUES 
    (?,?,?,?)""" 
    c.execute(query,(
        cur_Comp_SSID,
        random.choice(Comp_names),
        c.execute("SELECT * FROM USER ORDER BY RANDOM() LIMIT 1").fetchall()[0][0],
        random.choice(Types)
    ) ) 

start_date1 = datetime.date(year=2019, month=1, day=1) 
end_date1 = datetime.date(year=2019, month=12, day=31) 
for i in range(10): 
    cur_SSID=c.execute("SELECT * FROM COMPUTER ORDER BY RANDOM() LIMIT 1").fetchall()[0][0]
    print(cur_SSID)
    c.execute('''INSERT INTO USAGE ( Date_time, 
    Prog_name, 
    SSID, 
    Work_time 
    ) VALUES (?, ?, ?, ?)''', 
    ( 
        fake.date_time_between(start_date=start_date1, end_date=end_date1), 
        random.choice(Prog_names), 
        cur_SSID,
        random.randint(1,100000)
    ) 
    ) 







conn.commit() 
conn.close()