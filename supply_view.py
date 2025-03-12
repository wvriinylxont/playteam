from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt
supply= Flask(__name__)

supply_list=[]
sno=1


@supply.route("/finance/list")
def finance_view():
	
	return render_template("finance/list.html")


@supply.route("/finance/process", methods=['post'])
def finance_process():
	global fno, price_result
	item = request.form.get('item')
	price= int(request.form.get('price'))
	date = dt.datetime.now().strftime('%Y-%m-%d')
	finance_dict={'fno':fno, 'item':item, 'price':price, 'date':date}
	finance_list.append(finance_dict)
	fno+=1
	for finance_dict in finance_list:
		price_result =3
	
	return redirect("/finance/list", price_result=price_result)

@finance.route('/finance/delete',methods=['post'])
def delete():
	pass







finance.run(debug=True)