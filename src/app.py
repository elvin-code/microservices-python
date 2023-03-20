import socket
from flask import Flask, jsonify, render_template

app = Flask(__name__)

#Fuction to fetch hostname and ip 
def fetchDetails():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/")
def hello_world():
    return "<p>Hello word!</p>"


@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route("/details")
def details():
    host_name, host_ip = fetchDetails()
    return render_template('index.html', HOSTNAME=host_name, HOSTIP=host_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)