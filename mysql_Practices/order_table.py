import db_config

cursor = db_config.mydb.cursor()

#Order BY ASC
# # sql = "select * from anime ORDER BY anime_name"

#Order by Desc
# sql = "select * from anime ORDER BY episodes DESC"

#Delete one row or data
sql = "delete from anime where episodes = 0"


# Prevent SQL Injection
# sql = "delete from anime where episodes = %s"
# val = ('Jujutsu kaisen 2',)

cursor.execute(sql)
db_config.mydb.commit()

print(cursor.rowcount,"Record deleted")


# result = cursor.fetchall()
# for x in result:
#     print(x)
