
from tabnanny import verbose
from pythonping import ping
from flask import Flask, render_template, request
import socket


app = Flask(__name__)

ip = "192.168.229.170"
port = 5357
msg = b"Hello World"

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/my-link/', methods = ["POST","GET"])
def my_link():
   sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   sock.sendto(msg,(ip, port))
   return "pinginging"


if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")


