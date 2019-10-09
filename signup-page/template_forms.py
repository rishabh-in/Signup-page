from flask import Flask,render_template, request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("t_f_main.html")

@app.route("/sign_up")
def sign_up():
    return render_template("t_f_sign.html")

@app.route("/final")
def final():
    mylist=(request.args)
    first_name=mylist.get("first")
    last_name=mylist.get("last")
    return render_template("t_f_final.html",first_name=first_name,last_name=last_name)