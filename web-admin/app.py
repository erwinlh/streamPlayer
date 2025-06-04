from flask import Flask, render_template, send_from_directory
import json

app = Flask(__name__, static_folder='static')

@app.route('/')
def dashboard():
    with open('../config/config.json') as f:
        config = json.load(f)
    return render_template('dashboard.html', current_url=config.get('stream_url', ''))

@app.route('/preview.jpg')
def preview():
    return send_from_directory('static', 'preview.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
