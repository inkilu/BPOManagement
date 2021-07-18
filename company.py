from flask import Blueprint,render_template,request,redirect,url_for,session,flash
from database import*
import uuid

company=Blueprint('company',__name__)

@company.route('/company_home')
def company_home():
	if session.get("lid"):
		return render_template("company_home.html")
	else:
		return redirect(url_for("public.login"))

@company.route('/company_client_services',methods=['get','post'])
def company_client_services():
	if session.get("lid"):
		data={}
		q="select * from clients where company_id='%s'"%(session['cid'])
		data['view']=select(q)
		return render_template("company_client_services.html",data=data)
	else:
		return redirect(url_for("public.login"))


@company.route('/company_manage_client_service',methods=['get','post'])
def company_manage_client_service():
	if session.get("lid"):
		data={}
		id=request.args['id']
		q="select * from `company_services` where company_id='%s'"%(session['cid'])
		data['sr']=select(q)
		if 'action' in request.args:
			action=request.args['action']
			sid=request.args['sid']
		else:
			action=None
		if action=='update':
			q="select * from client_services inner join company_services using(services_id) where services_id='%s'"%(sid)
			data['update_view']=select(q)
		if 'update_submit' in request.form:
			sr=request.form['sr']
			date=request.form['date']
			q="update client_services  set services_id='%s',`started_date`='%s' where services_id='%s'"%(sr,date,sid)
			update(q)
			flash("Changes Saved")
			return redirect(url_for('company.company_manage_client_service',id=id))
		if action=='delete':
			q="delete from client_services where services_id='%s'"%(sid)
			delete(q)
		if 'submit' in request.form:
			sr=request.form['sr']
			date=request.form['date']
			q="insert into client_services (`client_id`,`services_id`,`started_date`,`current_status`) values('%s','%s','%s','pending')"%(id,sr,date)
			insert(q)
			flash("inserted")
			return redirect(url_for('company.company_manage_client_service',id=id))
		q="select * from clients inner join client_services using(client_id) inner join company_services using(services_id) where client_id='%s'"%(id)
		data['view']=select(q)
		return render_template("company_manage_client_service.html",data=data)
	else:
		return redirect(url_for("public.login"))

# company_client_services.html
@company.route('/company_manage_client_details',methods=['get','post'])
def company_manage_client_details():
	if session.get("lid"):
		data={}
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="delete from clients where client_id='%s'"%(id)
			delete(q)
			flash("deleted")
			return redirect(url_for("company.company_manage_client_details"))

		if action=='update':
			q="select * from clients where client_id='%s'"%(id)
			data['update_view']=select(q)

		if 'update_submit' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			hname=request.form['hname']
			place=request.form['place']
			phone=request.form['phone']
			email=request.form['email']
			pin=request.form['pin']
			q="update clients set first_name='%s',last_name='%s',phone='%s',email='%s',house_name='%s',place='%s',pincode='%s' where client_id='%s'"%(fname,lname,phone,email,hname,place,pin,id)
			update(q)
			flash("Changes Saved")
			return redirect(url_for("company.company_manage_client_details"))

		if 'submit' in request.form:
			fname=request.form['fname']
			lname=request.form['lname']
			hname=request.form['hname']
			place=request.form['place']
			phone=request.form['phone']
			email=request.form['email']
			pin=request.form['pin']
			q="insert into clients values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(session['cid'],fname,lname,phone,email,hname,place,pin)
			insert(q)
			flash("Client Added")
			return redirect(url_for("company.company_manage_client_details"))
		q="select * from clients where company_id='%s'"%(session['cid'])
		data['view']=select(q)
		return render_template("company_manage_client_details.html",data=data)
	else:
		return redirect(url_for("public.login"))

@company.route('/company_manage_services',methods=['get','post'])
def company_manage_services():
	if session.get("lid"):
		data={}
		if 'action' in request.args:
			action=request.args['action']
			id=request.args['id']
		else:
			action=None
		if action=='delete':
			q="delete from company_services where services_id='%s'"%(id)
			delete(q)
			flash("deleted")
			return redirect(url_for("company.company_manage_services"))

		if action=='update':
			q="select * from company_services where services_id='%s'"%(id)
			data['update_view']=select(q)

		if 'update_submit' in request.form:
			title=request.form['title']
			desc=request.form['desc']
			cr=request.form['cr']
			dur=request.form['dur']
			q="update company_services set service_title='%s',description='%s',charge_for_service='%s',service_duration='%s' where services_id='%s'"%(title,desc,cr,dur,id)
			update(q)
			flash("Changes Saved")
			return redirect(url_for("company.company_manage_services"))

		if 'submit' in request.form:
			title=request.form['title']
			desc=request.form['desc']
			cr=request.form['cr']
			dur=request.form['dur']
			q="insert into company_services values(null,'%s','%s','%s','%s','%s')"%(session['cid'],title,desc,cr,dur)
			insert(q)
			flash("Services Added")
			return redirect(url_for("company.company_manage_services"))
		
		q="select * from company_services where company_id='%s'"%(session['cid'])
		data['view']=select(q)
		return render_template("company_manage_services.html",data=data)
	else:
		return redirect(url_for("public.login"))

@company.route('/company_view_client_calls')
def company_view_client_calls():
	if session.get("lid"):
		data={}
		q="SELECT *,client_calls.description as ds FROM client_calls INNER JOIN clients USING(client_id) INNER JOIN companies USING(company_id) where company_id='%s'"%(session['cid'])
		data['view']=select(q)
		return render_template("company_view_client_calls.html",data=data)
	else:
		return redirect(url_for("public.login"))



@company.route('/company_view_status_of_client_calls',methods=['get','post'])
def company_view_status_of_client_calls():
	if session.get("lid"):
		call_id=request.args['id']
		data={}
		q="select *,client_calls.description as ds from client_calls inner join clients using(client_id) inner join client_call_updates using(call_id) inner join companies using(company_id) where client_calls.call_id='%s'"%(call_id)
		data['view']=select(q)
		return render_template("company_view_status_of_client_calls.html",data=data)
	else:
		return redirect(url_for("public.login"))

