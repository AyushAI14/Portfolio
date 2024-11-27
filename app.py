from flask import Flask, render_template,url_for

app = Flask(__name__,template_folder='templates',static_folder='static',static_url_path='/')
@app.route('/')
def home():
    return render_template('Index.html')
