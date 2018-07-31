import os
from flask import Flask
from flask import request
import requests
import sys
if sys.version < '3':
    reload(sys)
    sys.setdefaultencoding('utf-8')
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

app = Flask(__name__)
app.debug = True

@app.route('/')
def so():
    r = requests.get("http://so.com")
    return r.text

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
