from flask import Flask, render_template
import paho.mqtt.client as mqtt


app = Flask(__name__)


direction = {"dire1" : "Up",
             "dire2" : "Left",
             "dire3" : "Down",
             "dire4" : "Right"}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test/robotloca")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

client = mqtt.Client()
client.on_connect = on_connect
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect("broker.emqx.io", 1883)
client.loop_start


@app.route("/")
def route():
   client.loop_start()
   client.publish("test/direction", "Dock", qos = 1)
   return render_template("index.html")


@app.route("/<string:dire>")
def start(dire):


   if dire == "Up":
      client.publish("test/direction", "Up", qos = 1)


   elif dire == "Left":
      client.publish("test/direction", "Left", qos = 1)


   elif dire == "Down":
      client.publish("test/direction", "Down", qos = 1)


   elif dire == "Right":
      client.publish("test/direction", "Right", qos = 1)



   return render_template("index.html") 



if __name__ == '__main__':

   app.run(debug = True, host = "0.0.0.0")
