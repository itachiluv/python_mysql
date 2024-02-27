import db_config 

print(db_config.mydb)

cursor = db_config.mydb.cursor()

# Database Create.
# cursor.execute('create database sampleDB') 

#Show Database
# cursor.execute('show databases')

# for x in cursor:
#     print (x)

#create Tabele ---> anime 
# cursor.execute('create table anime (anime_name VARCHAR(255), episodes INT(6))')

# alter table:
# cursor.execute('alter table anime add column id INT AUTO_INCREMENT PRIMARY KEY')

# Insert tables

sql = ('insert into anime (anime_name,episodes) values (%s,%s)')

# single values
val = ("Dragon Ball Super","220")

# Execute single values
cursor.execute(sql,val)

#many Values
# val = [
#     ('Naruto','750'),
#     ('Boruto','250'),
#     ('Jujutsu Kaisen','')
# ]
# cursor.executemany(sql,val) #to execute many data in values.
db_config.mydb.commit()

print(cursor.lastrowid,"Inserted Successfully")