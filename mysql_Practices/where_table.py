import db_config

cursor = db_config.mydb.cursor()

#fetch 
# sql = "select * from anime where episodes = 24"


# wildcard Characters like search 
# sql = "select * from anime where anime_name LIKE '%o%'"

#prevent SQL Injection
sql = "select * from anime where anime_name = %s"
val = ("Dragon Ball 2",)

cursor.execute(sql,val)

result = cursor.fetchall()

for x in result:
    print(x)