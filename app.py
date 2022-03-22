from flask import Flask, render_template
import os

ip_list = ['192.168.229.158']
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/', methods = ['POST', 'GET'])
def my_link():
        response = os.system('ping -n 4 192.168.229.158')
        if "Received = 4":
            print(f"UP 192.168.229.158 Ping Successful")

            return 'Ping Successful'
        else:
            print(f"DOWN 192.168.229.158 Ping Unsuccessful")  

            return 'Ping Unsuccessful'
        

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")
