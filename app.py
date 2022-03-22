from flask import Flask, render_template
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import os


app = Flask(__name__)
hostname = "192.168.229.158" #example
response = os.system("ping -n 1 " + hostname)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/my-link/', methods = ['POST', 'GET'])
def my_link():
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-n'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '4', hostname]
    if response == 0:
     print (hostname, 'is up!')
    else:
     print (hostname, 'is down!')

    return subprocess.call(command) == 0 and 'ping succesful'
             
    

if __name__ == '__main__':
  app.debug = True
  app.run(host="0.0.0.0")
