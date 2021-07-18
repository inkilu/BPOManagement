from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from database import*
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	if session.get("lid"):
		return render_template("admin_home.html")
	else:
		return redirect(url_for("public.login"))


@admin.route('/admin_add_merchant_companies',methods=['get','post'])
def admin_add_merchant_companies():
	if session.get("lid"):
		data={}
		if 'submit' in request.form:
			cname=request.form['cname']
			work=request.form['work']
			desc=request.form['desc']
			phone=request.form['phone']
			email=request.form['email']
			web=request.form['web']
			q="INSERT into login values(null,'%s','%s','company')"%(email,phone)
			id=insert(q)
			q="INSERT INTO companies (login_id,`company_name`,`mode_of_work`,`description`,`phone`,`email`,`website`) VALUES('%s','%s','%s','%s','%s','%s','%s')"%(id,cname,work,desc,phone,email,web)
			insert(q)
			flash("Added")
			return redirect(url_for("admin.admin_add_merchant_companies"))
		if 'remove_id' in request.args:
			id=request.args['remove_id']
			q="delete from companies where login_id='%s'"%(id)
			delete(q)
			q="delete from login where login_id='%s'"%(id)
			delete(q)
			flash("deleted")
			return redirect(url_for("admin.admin_add_merchant_companies"))
		q="select * from companies"
		data['view']=select(q)
		return render_template("admin_add_merchant_companies.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route('/admin_assigns_staffs_to_desired_companies',methods=['get','post'])
def admin_assigns_staffs_to_desired_companies():
	if session.get("lid"):
		return render_template("admin_assigns_staffs_to_desired_companies.html")
	else:
		return redirect(url_for("public.login"))


@admin.route('/admin_generate_notifications',methods=['get','post'])
def admin_generate_notifications():
	if session.get("lid"):
		data={}
		q="select * from staffs"
		data['staffa']=select(q)
		if 'submit' in request.form:
			staff=request.form['staff']
			msg=request.form['msg']
			q="INSERT into notifications values(NULL,'%s','%s','pending',curdate())"%(staff,msg)
			insert(q)
			flash("Notification Sent!!!")
			return redirect(url_for("admin.admin_generate_notifications"))
		q="select * from notifications inner join staffs using(staff_id) order by date desc"
		data['view']=select(q)
		return render_template("admin_generate_notifications.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route('/admin_view_companies',methods=['get','post'])
def admin_view_companies():
	if session.get("lid"):
		data={}
		q="select * from companies"
		data['view']=select(q)
		return render_template("admin_view_companies.html",data=data)
	else:
		return redirect(url_for("public.login"))


@admin.route('/admin_staff_registration',methods=['get','post'])
def admin_staff_registration():
	if session.get("lid"):
		data={}
		q="select *from companies"
		data['cmp']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='update':
			q="select *,staffs.phone as sp,staffs.email as se from staffs inner join login on login.login_id=staffs.login_id inner join companies using(company_id) where staffs.login_id='%s'"%(id)
			data['update_view']=select(q)

		if 'update_submit' in request.form:
			cname=request.form['cname']
			usertype=request.form['usertype']
			fname=request.form['fname']
			lname=request.form['lname']
			phone=request.form['phone']
			email=request.form['email']
			photo=request.files['photo']
			path="static/"+str(uuid.uuid4())+photo.filename
			photo.save(path)
			gender=request.form['gender']
			age=request.form['age']
			q="update login set username='%s',password='%s',usertype='%s' where login_id='%s'"%(email,phone,usertype,id)
			update(q)
			if photo.filename:
				q="update staffs set `company_id`='%s',`first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`photo`='%s',`gender`='%s',age='%s' where login_id='%s'"%(cname,fname,lname,phone,email,path,gender,age,id)
				update(q)
				flash("Updated")
				return redirect(url_for("admin.admin_staff_registration"))
			else:
				q="update staffs set `company_id`='%s',`first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`gender`='%s',age='%s' where login_id='%s'"%(cname,fname,lname,phone,email,gender,age,id)
				update(q)
				flash("Updated")
				return redirect(url_for("admin.admin_staff_registration"))
# update_submit
		if action=='delete':
			q="delete from staffs where login_id='%s'"%(id)
			delete(q)
			q="delete from login where login_id='%s'"%(id)
			delete(q)
			flash("Deleted")
			return redirect(url_for('admin.admin_staff_registration'))
		if 'submit' in request.form:
			cname=request.form['cname']
			usertype=request.form['usertype']
			fname=request.form['fname']
			lname=request.form['lname']
			phone=request.form['phone']
			email=request.form['email']
			photo=request.files['photo']
			path="static/"+str(uuid.uuid4())+photo.filename
			photo.save(path)
			gender=request.form['gender']
			age=request.form['age']
			q="insert into login values(null,'%s','%s','%s')"%(email,phone,usertype)
			id=insert(q)
			q="insert into staffs (`login_id`,`company_id`,`first_name`,`last_name`,`phone`,`email`,`photo`,`gender`,`age`) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,cname,fname,lname,phone,email,path,gender,age)
			insert(q)
			flash("Registered")
			return redirect(url_for("admin.admin_staff_registration"))
		q="select*,staffs.phone as sp,staffs.email as se,staffs.login_id as sl from staffs inner join companies using(company_id) inner join login on login.login_id=staffs.login_id"
		data['view']=select(q)
		return render_template("admin_staff_registration.html",data=data)
	else:
		return redirect(url_for("public.login"))



@admin.route('/admin_view_client_calls',methods=['get','post'])
def admin_view_client_calls():
	if session.get("lid"):
		data={}
		q="SELECT *,client_calls.description as ds FROM client_calls INNER JOIN clients USING(client_id) INNER JOIN companies USING(company_id)"
		data['view']=select(q)
		return render_template("admin_view_client_calls.html",data=data)
	else:
		return redirect(url_for("public.login"))

@admin.route('/admin_view_client_details',methods=['get','post'])
def admin_view_client_details():
	if session.get("lid"):
		data={}
		id=request.args['id']
		q="select * from clients inner join companies using(company_id) where company_id='%s'"%(id)
		data['view']=select(q)
		return render_template("admin_view_client_details.html",data=data)
	else:
		return redirect(url_for("public.login"))



@admin.route('/admin_view_status_of_client_calls',methods=['get','post'])
def admin_view_status_of_client_calls():
	if session.get("lid"):
		call_id=request.args['id']
		data={}
		q="select *,client_calls.description as ds from client_calls inner join clients using(client_id) inner join client_call_updates using(call_id) inner join companies using(company_id) where client_calls.call_id='%s'"%(call_id)
		data['view']=select(q)
		return render_template("admin_view_status_of_client_calls.html",data=data)
	else:
		return redirect(url_for("public.login"))


# @admin.route('/admin_attendance',methods=['get','post'])
# def admin_attendance():
# 	if session.get("lid"):
# 		return render_template("admin_attendance.html")
# 	else:
# 		return redirect(url_for("public.login"))