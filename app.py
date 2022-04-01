from flask import Flask, render_template
import paho.mqtt.client as mqtt

app = Flask(__name__)
ip_list = {"addr": "192.168.229.170"}

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/mylink/<string:ip_list>', methods = ["GET"])
def my_link(ip_list):
   client = mqtt.Client()
   client.connect_async("driver.cloudmqtt.com", 18626)
   return {"pinged": ip_list}



if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
