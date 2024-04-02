try:
    from flask import Flask, render_template
    import os,sys
except ModuleNotFoundError as e:
    print(str(e))

app = Flask(__name__, template_folder="templates")
selected = None

@app.route('/')
def fake_page():
    return render_template(selected)

if __name__ == "__main__":
    
    app.run(debug=True)