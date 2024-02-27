import db_config 
import json

cursor = db_config.mydb.cursor()

# Select all Column
cursor.execute('select * from anime LIMIT 5 ')  #set limitation 

#Select one or 2 column
# cursor.execute('select id,anime_name from anime')

result = cursor.fetchall() #fetchall method

for i in result:
    print(json.dumps(i))

# result = cursor.fetchone()
# print(result)


