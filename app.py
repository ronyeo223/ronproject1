from flask import Flask, render_template
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))

app = Flask(__name__)
ip_list = {"addr": "192.168.229.170"}


@app.route('/')
def index():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.username_pw_set("esznwayl","gqXdqVuApw95")
    client.connect("driver.cloudmqtt.com", 18626, 60)
    client.loop_forever()
   return render_template('index.html')

@app.route('/mylink/<string:ip_list>', methods = ["GET"])
def my_link(ip_list):
   client.publish("$SYS/#", "Hello World", qos = 1)
   return {"pinged": ip_list}



if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")

