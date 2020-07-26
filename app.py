from flask import Flask, render_template, request, redirect, url_for, jsonify, Response

import re
app = Flask(__name__)


# LOGIN
@app.route('/')
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usern = request.form.get("username").upper()
        passw = request.form.get("password")

        if re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6}$",passw) and re.search("[^0-9]",usern):
            data = {    
                "status": 200,
                "msg": "Success"
                 }
        else:
            data=  {    
                "status": 202,
                "msg": "Failure: password to have 1 character and 1 number"
                  }
            
        if len(passw)!=6 and re.search("[^0-9]",usern):
            data = {
                    "status": 201,
                    "msg": "Failure: password should be of length 6"
                    }
        if re.search("[0-9]",usern):
            data={
                "status": 203,
                "msg": "Failure: only characters allowed in username"
                    }
        return jsonify(data)
    return render_template("login.html")
    
# Main
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
