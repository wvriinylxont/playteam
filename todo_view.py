from flask import Flask, Blueprint, render_template, redirect, request
import datetime

todo_app = Flask(__name__)

todos = []
tno = 1
@todo_app.route("/")
def home():
    return render_template("index.html")

@todo_app.route("/todo/list")
def list_todos():
    return render_template("todo/list.html", todos=todos)

@todo_app.route("/todo/insert", methods=["post"])
def insert():
    global tno
    title = request.form.get("title")
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    new_todo = {"tno":tno, "title":title, "date":date_str, "finish":False}
    todos.append(new_todo)
    tno+=1
    return redirect("/todo/list")

@todo_app.route("/todo/delete", methods=["post"])
def delete():
    tno_to_delete = int(request.form.get("tno"))
    global todos
    todos = [todo for todo in todos if todo["tno"] != tno_to_delete]
    return redirect("/todo/list")



todo_app.run(debug=True)