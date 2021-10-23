import time
from flask import Flask

app = Flask(__name__)

@app.route('/text')
def get_current_text():
    return {'time': time.time()}
  