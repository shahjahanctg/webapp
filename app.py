import socket
import platform
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def display_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    system_info = f'{platform.system()} {platform.release()}'

    return render_template('info.html', hostname=hostname, ip_address=ip_address, system_info=system_info)

if __name__ == '__main__':
    app.run()
