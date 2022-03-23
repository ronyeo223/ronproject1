
from flask import Flask, render_template
import os
import socket

ip_list = ['192.168.229.158']
app = Flask(__name__)

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("https://certisproject1222222222.herokuapp.com/", 1024))
s.listen(5)



@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/', methods = ['POST', 'GET'])
def my_link():
  while True:
     response = os.system('ping -n 4 192.168.229.170')
     if "Received = 4":
            print(f"UP 192.168.229.170 Ping Successful")
            clientsocket, address = s.accept()
            print(f"connection from {address} has been established!")
            clientsocket.send(bytes("welcome to the server", "utf-8"))
            return 'Ping Successful'

     else:
            print(f"DOWN 192.168.229.170 Ping Unsuccessful")  

            return 'Ping Unsuccessful'
        

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")

        
