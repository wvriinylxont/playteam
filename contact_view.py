from flask import Flask, Blueprint, render_template,redirect, request
import datetime as dt

contact_app=Blueprint('contact_app',__name__)

tels=[]
telno=1

@contact_app.route('/contact/list')
def index():
    return render_template('/contact/list.html', tels=tels)

@contact_app.route('/contact/write', methods=['post'])
def write():
    global telno
    name=request.form.get('name')
    tel=request.form.get('tel')
    address=request.form.get('address')
    new_tel={'telno':telno, 'name': name, 'tel':tel, 'address':address}
    tels.append(new_tel)
    telno+=1
    return redirect('/contact/list')

@contact_app.route('/contact/delete', methods=['post'])
def delete():
    telno=int(request.form.get('telno'))
    for contact in tels:
        if contact['telno']==telno:
            tels.remove(contact)
    return redirect('/contact/list')
