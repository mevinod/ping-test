# app.py
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def perform_ping(host):
    try:
        # Perform ping test
        ping_result = subprocess.run(['ping', '-c', '4', host], capture_output=True, text=True)
        return ping_result.stdout
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        host = request.form['host']
        ping_result = perform_ping(host)
        return render_template('index.html', ping_result=ping_result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

