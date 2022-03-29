
from tabnanny import verbose
from pythonping import ping
from flask import Flask, render_template, request
import os
import asyncio
from websockets import serve

app = Flask(__name__)

ip_list = ["192.168.229.170"]

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/my-link/', methods = ["POST","GET"])
def my_link():
       response = ping('192.168.229.170', verbose= True)
       if response.rtt_avg_ms >= 0.07 :
                print(f"UP 192.168.229.170 Ping Successful")
                
                return 'Ping Successful'

       else:
                print(f"DOWN 192.168.229.170 Ping Unsuccessful")  
                return 'Ping Unsuccessful'

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")


