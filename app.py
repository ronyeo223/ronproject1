from flask import Flask, render_template
import paho.mqtt.client as mqtt



app = Flask(__name__)

global y
y = 0
global x
x = 0

direction = {"dire1" : "Up",
             "dire2" : "Left",
             "dire3" : "Down",
             "dire4" : "Right"}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish 
client.username_pw_set("esznwayl","gqXdqVuApw95")
client.connect("broker.emqx.io", 1883)


@app.route("/")
def route():
   client.publish("$SYS/robot", "Dock", qos = 1)
   return render_template("index.html")


@app.route("/<string:dire>")
def start(dire):
   global y
   global x
   n=25

   client.loop_start
   if dire == "Up":
      y += n
      client.publish("$SYS/direction", "Up", qos = 1)
      client.publish("$SYS/robot",f"x = {x}, y = {y}" )

   elif dire == "Left":
      x -= n
      client.publish("$SYS/direction", "Left", qos = 1)
      client.publish("$SYS/robot",f"x = {x}, y = {y}" )

   elif dire == "Down":
      y -= n
      client.publish("$SYS/direction", "Down", qos = 1)
      client.publish("$SYS/robot",f"x = {x}, y = {y}" )

   elif dire == "Right":
      x += n
      client.publish("$SYS/direction", "Right", qos = 1)
      client.publish("$SYS/robot",f"x = {x}, y = {y}" )


   client.loop_stop

   return render_template("index.html")



if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0")



