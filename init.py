from flask import Flask, request, render_template, redirect
from settings import write_config, get_config
from server_manager import load_servers, get_servers

app = Flask(__name__)

@app.route('/')
def home():
    servers = get_servers()
    return render_template("index.html", servers=servers)


@app.route('/autoload-servers', methods=['POST'])
def autoload_servers():
    load_servers()
    return redirect('/')


@app.route('/settings')
def settings():
    config = get_config()
    return render_template("settings.html", default_server_path=config.get('default_server_path'))


@app.route('/submit-setting', methods=['POST'])
def submit_settings():
    write_config(request.form.to_dict())
    config = get_config()
    return render_template("settings.html", default_server_path=config.get('default_server_path'))
    
