from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from database import*
import uuid

customer_care=Blueprint('customer_care',__name__)

@customer_care.route('/customer_care_home')
def customer_care_home():
	if session.get("lid"):
		return render_template("customer_care_home.html")
	else:
		return redirect(url_for("public.login"))

@customer_care.route('/customer_care_update_client_call',methods=['get','post'])
def customer_care_update_client_call():
	if session.get("lid"):
		data={}
		q="SELECT *,client_calls.`description` as des FROM client_calls INNER JOIN clients USING(client_id) INNER JOIN companies USING(company_id) INNER JOIN staffs ON companies.`company_id`=staffs.`company_id` WHERE staffs.`staff_id`='%s'"%(session['ccid'])
		data['view']=select(q)
		if 'ccid' in request.args:
			id=request.args['ccid']
			q="select * from client_call_updates where call_id='%s'"%(id)
			res=select(q)
			if res:
				return redirect(url_for("customer_care.customer_care_update_call_status",id=id))
			else:
				flash("Not Updated...")
		return render_template("customer_care_update_client_call.html",data=data)
	else:
		return redirect(url_for("public.login"))

@customer_care.route('/customer_care_update_profile',methods=['get','post'])
def customer_care_update_profile():
	if session.get("lid"):
		data={}
		q="select *,staffs.phone as sp,staffs.email as se from staffs inner join login on login.login_id=staffs.login_id inner join companies using(company_id) where staff_id='%s'"%(session['ccid'])
		data['update_view']=select(q)

		if 'update_submit' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			phone=request.form['phone']
			email=request.form['email']
			photo=request.files['photo']
			path="static/"+str(uuid.uuid4())+photo.filename
			photo.save(path)
			gender=request.form['gender']
			age=request.form['age']
			if photo.filename:
				q="update staffs set `first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`photo`='%s',`gender`='%s',age='%s' where staff_id='%s'"%(fname,lname,phone,email,path,gender,age,session['ccid'])
				update(q)
				flash("Updated")
				return redirect(url_for("customer_care.customer_care_update_profile"))
			else:
				q="update staffs set `first_name`='%s',`last_name`='%s',`phone`='%s',`email`='%s',`gender`='%s',age='%s' where staff_id='%s'"%(fname,lname,phone,email,gender,age,session['ccid'])
				update(q)
				flash("Updated")
				return redirect(url_for("customer_care.customer_care_update_profile"))
		return render_template("customer_care_update_profile.html",data=data)
	else:
		return redirect(url_for("public.login"))

@customer_care.route('/customer_care_view_escalated_complaints')
def customer_care_view_escalated_complaints():
	if session.get("lid"):
		return render_template("customer_care_view_escalated_complaints.html")
	else:
		return redirect(url_for("public.login"))

@customer_care.route('/customer_care_view_notifications',methods=['get','post'])
def customer_care_view_notifications():
	if session.get("lid"):
		data={}
		q="SELECT * FROM notifications WHERE staff_id='%s'"%(session['ccid'])
		res=select(q)
		data['view']=res
		i=1
		for row in data['view']:
			if 'submit'+str(i) in request.form:
				reply=request.form['reply'+str(i)]
				q="update notifications set reply='%s' where notification_id='%s'"%(reply,res[i-1]['notification_id'])
				update(q)
				flash("Replied")
				return redirect(url_for("customer_care.customer_care_view_notifications"))
			i=i+1
		return render_template("customer_care_view_notifications.html",data=data)
	else:
		return redirect(url_for("public.login"))


@customer_care.route('/customer_care_update_call_status',methods=['get','post'])
def customer_care_update_call_status():
	if session.get("lid"):
		call_id=request.args['id']
		data={}
		q="select *,client_calls.description as ds from client_calls inner join clients using(client_id) inner join client_call_updates using(call_id) inner join companies using(company_id) inner join staffs on staffs.company_id=clients.company_id where client_calls.call_id='%s' and staffs.staff_id='%s'"%(call_id,session['ccid'])
		data['view']=select(q)
		return render_template("customer_care_update_call_status.html",data=data)
	else:
		return redirect(url_for("public.login"))