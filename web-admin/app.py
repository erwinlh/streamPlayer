from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import json
import subprocess
import os

app = Flask(__name__, static_folder='static')
app.secret_key = 'supersecretkey'  # Cambiar en producción

USER = 'admin'
PASSWORD = 'streamer'

CONFIG_PATH = '../config/config.json'
STREAM_SCRIPT = '../streamer/start_stream.sh'

def read_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def write_config(data):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == USER and request.form['password'] == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    config = read_config()
    return render_template('dashboard.html', current_url=config.get('stream_url', ''))

@app.route('/update', methods=['POST'])
def update_url():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    new_url = request.form.get('new_url')
    config = read_config()
    config['stream_url'] = new_url
    write_config(config)
    subprocess.run(['pkill', '-f', 'mpv'])  # Detiene cualquier instancia de mpv
    subprocess.Popen(['bash', STREAM_SCRIPT])
    return redirect(url_for('dashboard'))

@app.route('/stop', methods=['POST'])
def stop_stream():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    subprocess.run(['pkill', '-f', 'mpv'])
    return redirect(url_for('dashboard'))

@app.route('/preview.jpg')
def preview():
    return send_from_directory('static', 'preview.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
