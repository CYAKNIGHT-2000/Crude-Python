import sqlite3
import cgi
data=cgi.FieldStorage()
id = data.getvalue('t1')
phone = data.getvalue('t2')
name = data.getvalue('t3')
db = sqlite3.connect('crude1.sqlite')
print('Content-type:text/html\r\n\r\n')
print("<body bgcolor='yellow' text='red'>")
print("</body>")

def updateSqliteTable(id, phone,name):
    try:
        cursor = db.cursor()
        qry = """Update pratik set phone = ?,name=? where id = ?"""
        data = (phone,name, id)
        cursor.execute(qry, data)
        db.commit()
        print("Record Updated successfully")
        cursor.close()
    except:
     print("error in operation")
    db.rollback()

updateSqliteTable(id, phone,name)
db.close()