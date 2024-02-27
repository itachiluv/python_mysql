import db_config

cursor = db_config.mydb.cursor()

# update row 
# sql = "update anime SET episodes = 1096 where episodes = 1095"

# SQL Injection 
sql = "update anime SET episodes = %s where episodes = %s"
val = ('255','250')
cursor.execute(sql,val)
db_config.mydb.commit()

print(cursor.rowcount,"Row Updated Succesfully")