from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)

direction = {"dire1" : "Forward",
             "dire2" : "Left",
             "dire3" : "Back",
             "dire4" : "Right"}


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))


client = mqtt.Client()


@app.route('/')
def index():

   client.on_connect = on_connect
   client.on_message = on_message
   client.on_publish = on_publish 
   client.username_pw_set("esznwayl","gqXdqVuApw95")
   client.connect("driver.cloudmqtt.com", 18626, 60)
   return render_template('index.html')

@app.route('/mylink/<string:dire>', methods = ["GET"])
def my_link1(dire):
   client.loop_start
   if dire == "dire1":
      client.publish("$SYS/direction", "Forward", qos = 1)
   
   elif dire == "dire2":
      client.publish("$SYS/direction", "Left", qos = 1)

   elif dire == "dire3":
      client.publish("$SYS/direction", "Back", qos = 1)

   elif dire == "dire4":
      client.publish("$SYS/direction", "Right", qos = 1)

   client.loop_stop
   return direction[dire]




if __name__ == '__main__':
   app.run(debug = True, host = "0.0.0.0")

