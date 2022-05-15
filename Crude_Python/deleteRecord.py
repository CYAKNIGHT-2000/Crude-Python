
import sqlite3
import cgi
data=cgi.FieldStorage()
id = data.getvalue('t1')
db = sqlite3.connect('crude1.sqlite')

print('Content-type:text/html\r\n\r\n')
print("<body bgcolor='yellow' text='red'>")
print("</body>")


def deleteSqliteRecord(id):
    try:
        cursor = db.cursor()
        sql_update_query = """DELETE from pratik where id = ?"""
        cursor.execute(sql_update_query, (id,))
        db.commit()
        print("Record deleted successfully")
        cursor.close()

    except:
     print("error in operation")
    db.rollback()

deleteSqliteRecord(id)
db.close()

