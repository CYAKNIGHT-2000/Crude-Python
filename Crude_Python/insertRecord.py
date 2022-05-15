

import sqlite3
import cgi
# name1 = input("StudentID:")
# phone = input("StudentPhoneNumber:")
data=cgi.FieldStorage()
name1=data.getvalue('Name')
phone=data.getvalue('PhoneNumber')
db = sqlite3.connect('crude1.sqlite')

print('Content-type:text/html\r\n\r\n')
print("<body bgcolor='yellow' text='red'>")
print("</body>")



qry= """
insert into pratik (name, phone) values('{}','{}');
""".format(
    name1,phone
)
try:
     cur = db.cursor()
     cur.execute(qry)
     db.commit()
     print('<h1>records added successfully</h1>')
     cur.close()
except:
     print ("error in operation")
     db.rollback()
db.close()
