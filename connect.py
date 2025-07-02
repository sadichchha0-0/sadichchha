import mariadb

try:
    connect=mariadb.connect(
       user="sadichchha",
       password="pass1",
       host="localhost",
       port=3306,
       database="studentdb"
    )
except Exception as e:
    print(f"Error:",e)

values_to_insert=[('jane','2003-03-24',''),('joe','2009-04-31')]
insert_stmt="""
insert into student(subent,birth of date,stubent email) values(?,?,?)
"""
cur=connect.cursor()
cur.executemany()
cur.execute("create database newdb")
cur.execute("commit")