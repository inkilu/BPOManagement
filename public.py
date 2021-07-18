from flask import Blueprint,url_for,request,redirect,render_template,session,flash
from database import*

public= Blueprint('public',__name__)

@public.route('/')
def home():
	session.clear()
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	session.clear()
	if 'submit' in request.form:
		uname=request.form['uname']
		passs=request.form['passs']

		q="select * from login where username='%s' and password='%s'"%(uname,passs)
		res=select(q)
		if res:
			session['lid']=res[0]['login_id']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.admin_home'))
			if res[0]['usertype']=='company':
				q1="select * from companies where login_id='%s'"%(res[0]['login_id'])
				res1=select(q1)
				print(q1)
				if res1:
					session['cid']=res1[0]['company_id']
					return redirect(url_for('company.company_home'))
					# c_care
			if res[0]['usertype']=='c_care':
				q1="select * from staffs where login_id='%s'"%(res[0]['login_id'])
				res1=select(q1)
				print(q1)
				if res1:
					session['ccid']=res1[0]['staff_id']
					return redirect(url_for('customer_care.customer_care_home'))

			if res[0]['usertype']=='technical':
				q1="select * from staffs where login_id='%s'"%(res[0]['login_id'])
				res1=select(q1)
				print(q1)
				if res1:
					session['sid']=res1[0]['staff_id']
					return redirect(url_for('technical.technical_home'))
			else:
				flash("Your Registration under-process... You Can not Login Now!")
		else:
			flash("Username or Password Not Correct")
			return redirect(url_for("public.home"))

	return render_template("login.html")