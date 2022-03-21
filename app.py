from flask import Flask, render_template, request
import os

ip_list = ['192.168.229.156']
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my-link():
    for ip in ip_list:
      response = os.system('ping -n 4 192.168.229.156')
      if response == 0 :

            print(f"UP {ip} Ping Successful")

            return 'Ping Successful'
      else:
            print(f"DOWN {ip} Ping Unsuccessful")  

            return 'Ping Unsuccessful'


if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")
