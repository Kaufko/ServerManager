from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/submit-setting', methods=['POST'])
def submit_settings():
    with open('config.json', 'w') as f:
        json.dump(request.form.to_dict(), f)
    return render_template('settings.html')
