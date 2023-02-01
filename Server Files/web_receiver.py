from flask import Flask, request
from flask import render_template
import cv2
import time
import main2 as principal
from flask import  render_template, jsonify, request
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.before_first_request
def loadData():
    print('doing something')
    global sign_recorder
    sign_recorder = principal.preproceso()


@app.route("/upload", methods=["POST"], strict_slashes=False)
def index2():
    if(request.method == "POST"):
        f =  request.files['file']
        print("Uploaded to server")
        filename = secure_filename(f.filename)
        f.save(os.path.join(filename))
        print("Starting preprocess")
        print(principal.proceso(sign_recorder))
        time.sleep(1)
        return 'YA UWU'


if __name__ == "__main__":
    app.run (host="0.0.0.0", port=5000,debug=True)