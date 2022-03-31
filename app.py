
from flask import Flask, render_template, request

app = Flask(__name__)

ip_list = {"addr": "192.168.229.159"}

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/mylink/<string:ip_list>', methods = ["POST", "GET"])
def my_link(ip_list):
   return {"pinged": ip_list}



if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")


