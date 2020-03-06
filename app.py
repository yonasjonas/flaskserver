from flask import Flask
import socket,json,psutil,multiprocessing
app = Flask(__name__)


@app.route('/')
def hello_world():

    info = {}
    info['hostname'] = socket.gethostname()
    info['ip-address'] = socket.gethostbyname(socket.gethostname())
    info['processor count'] = multiprocessing.cpu_count()
    info['pram'] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
    return json.dumps(info, sort_keys=True, indent=444)


if __name__ == '__main__':

    debug = True
    app.run(host='127.0.0.1', port=8080)
