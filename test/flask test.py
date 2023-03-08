from flask import Flask, request
from flask import render_template
from tesM import parallel_process
from flask import  render_template, jsonify, request
import os
import time

import webbrowser

from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/test")
def testing():
    parallel_process()
    print('TESTING ZONE   ')
    return 'si'
    
if __name__ == "__main__":
    app.run (host="0.0.0.0", port=5000,debug=True, use_reloader=False)