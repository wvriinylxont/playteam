from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt
supply_app= Flask(__name__)

supply_list=[]
sno=1


@supply_app.route("/supply/list")
def finance_view():
	
	return render_template("supply/list.html",supply_list=supply_list)


@supply_app.route("/supply/process", methods=['post'])
def finance_process():
	global sno
	item = request.form.get('item')
	count= int(request.form.get('count'))
	supply_dict={'sno':sno, 'item':item, 'count':count}
	supply_list.append(supply_dict)
	sno+=1
	return redirect("/supply/list")

@supply_app.route("/supply/count_plus",methods=['post'])
def count_plus():
	count= int(request.form.get('count'))
	sno = int(request.form.get('sno'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_dict['count']=count+1
			break
	return redirect("/supply/list")

@supply_app.route("/supply/count_minus",methods=['post'])
def count_minus():
	count= int(request.form.get('count'))
	sno = int(request.form.get('sno'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_dict['count']=count-1
			break
	return redirect("/supply/list")

@supply_app.route('/supply/delete',methods=['post'])
def delete():
	sno = int(request.form.get('sno'))
	for supply_dict in supply_list:
		if supply_dict['sno']==sno:
			supply_list.remove(supply_dict)
	return redirect("/supply/list")







supply_app.run(debug=True)