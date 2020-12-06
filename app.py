#!/home/rajesh/projects/endpoint/env/bin/python3
from flask import Flask
from flask import request
import csv

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!\n"

@app.route('/data', methods=['GET', 'POST'])
def data():
    host = request.args.get('host')
    utime = request.args.get('utime')
    kernel = request.args.get('kver')
    with open('/tmp/data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([host,utime,kernel])
    return "host: {} is up from {} and its running on  kernel version: {}\n".format(host,utime,kernel)

if __name__ == '__main__':
    app.run()

