import asyncio
import websockets
from flask import Flask, render_template, request
import os


ip_list = ['192.168.229.170']
app = Flask(__name__)
async def handler(websocket, path):
 
    data = await websocket.recv()
    reply = f"Data recieved as:  {data}!"
    await websocket.send(reply)
    start_server = websockets.serve(handler, "192.168.229.170", 5000)
    await asyncio.Future()

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/my-link/', methods = ["POST", "GET"])
async def my_link():
       response = os.system('ping -n 4 192.168.229.170')
       if "Received = 4":
                print(f"UP 192.168.229.170 Ping Successful")
                return 'Ping Successful'

       else:
                print(f"DOWN 192.168.229.170 Ping Unsuccessful")  
                return 'Ping Unsuccessful'



if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")


