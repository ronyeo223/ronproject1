
from flask import Flask, render_template, request
from websockets import serve

app = Flask(__name__)

ip_list = {"addr": "192.168.229.159"}

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/mylink/<string:ping>', methods = ["POST"])
def my_link(ping):
   return {"pinged": ping}



if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")


