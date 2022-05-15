
import sqlite3
db = sqlite3.connect('crude1.sqlite')
print('Content-type:text/html\r\n\r\n')
print("<body bgcolor='yellow' text='red'>")
print("</body>")
qry = "Select * from pratik"
try:
    cur = db.cursor()
    cur.execute(qry)
    for row in cur:
      print(row)  
      print("<br>")
    cur.close()
except:
    print("error in operation")
    db.rollback()
db.close()
