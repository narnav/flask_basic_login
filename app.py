from flask import Flask, render_template, request
api = Flask(__name__)

users=[{"user":"waga","pwd":"123"},{"user":"baga","pwd":"123"}]

@api.route('/')
def hello():
    return render_template("index.html")

@api.route('/login',methods=["GET","POST"] )
def login():
    if request.method == "POST":
        user =request.form["user"]
        pwd =request.form["pwd"]
        for usr in users:
            if user ==usr["user"] and pwd ==usr["pwd"]:
                return render_template("success.html",welc_user=user)            
    return render_template("login.html")


if __name__ == '__main__':
    api.run(debug=True)