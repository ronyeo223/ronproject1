
from http import client
from flask import Flask, render_template
from flask_socketio import socketio, emit
import os
import socket


ip_list = ['192.168.229.170']
app = Flask(__name__)

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('192.168.229.170', 5000))
s.listen(5)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/my-link/')
def my_link():

     response = os.system('ping -n 4 192.168.229.170')
     if "Received = 4":
            print(f"UP 192.168.229.170 Ping Successful")
            return 'Ping Successful'

     else:
            print(f"DOWN 192.168.229.170 Ping Unsuccessful")  

            return 'Ping Unsuccessful'

@socketio.event
def pingevent(ping):
       socketio.emit('web_BBBWEvent', ping)

       
if __name__ == '__main__':
  app.debug = True
  socketio.run(app)
        
