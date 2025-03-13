from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt
finance_app= Blueprint('finance_app',__name__)

finance_list=[]
fno=1
price_total=0

@finance_app.route("/")
def home():
    return render_template("index.html")

@finance_app.route("/finance/list")
def finance_view():
	global price_total
	price_total=0
	for finance_dict in finance_list:
		price_total += finance_dict['price']

	return render_template("finance/list.html",finance_list=finance_list,price_total= price_total)

@finance_app.route("/finance/process", methods=['post'])
def finance_process():
	global fno 
	item = request.form.get('item')
	price= int(request.form.get('price'))
	date = dt.datetime.now().strftime('%Y-%m-%d')
	finance_dict={'fno':fno, 'item':item, 'price':price, 'date':date}
	finance_list.append(finance_dict)
	fno+=1
	return redirect("/finance/list")

@finance_app.route('/finance/delete',methods=['post'])
def delete():
	fno= int(request.form.get('fno'))
	for finance_dict in finance_list:
		if finance_dict['fno']==fno:
			finance_list.remove(finance_dict)
	return redirect("/finance/list")







