import mysql.connector
user="root"
passs=""
database="bpo_management"
# employee_attendance

def select(q):
	con=mysql.connector.connect(user=user,password=passs,host="localhost",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	res=cur.fetchall()
	cur.close()
	con.close()
	return res

def insert(q):
	con=mysql.connector.connect(user=user,password=passs,host="localhost",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	res=cur.lastrowid
	cur.close()
	con.close()
	return res	

def update(q):
	con=mysql.connector.connect(user=user,password=passs,host="localhost",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	res=cur.rowcount
	cur.close()
	con.close()
	return res

def delete(q):
	con=mysql.connector.connect(user=user,password=passs,host="localhost",database=database)
	cur=con.cursor(dictionary=True)
	cur.execute(q)
	con.commit()
	res=cur.rowcount
	cur.close()
	con.close()
	return res