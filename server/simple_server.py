from flask import Flask, flash, request, send_from_directory, redirect, url_for, jsonify
import stego_functions as sf
import skimage.io as skio
import png
import flask_cors
import os
import string
import random
from decorator import crossdomain
from time import sleep

app = Flask(__name__)
flask_cors.CORS(app)

DECODED_FOLDER='.'
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {
        "encode": ['png', 'jpg', 'jpeg'],
        "decode": ['png']
        }

decoded_images = []
encoded_images = []

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

def removeTempFiles(images):
    for i in images:
        if os.path.exists(i):
            os.remove(i)

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def allowed_file(filename, version):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[version]

@app.route('/decode', methods=['POST'])
def upload_file_decode():
    removeTempFiles(decoded_images)
    with open("uploaded-for-decoding.png", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
        base = skio.imread('uploaded-for-decoding.png')
    filename = "decoded" + id_generator()
    sf.saveDecoded(base, filename)
    imageurl = filename + ".png"
    decoded_images.append(imageurl)
    urldict = {"url": imageurl}
    if(os.path.exists("uploaded-for-decoding.png")):
        os.remove("uploaded-for-decoding.png")
    return jsonify(urldict)

@app.route('/<filename>')
@crossdomain(origin='*')
def uploaded_file(filename):
    return send_from_directory('.',
                               filename)
@app.route('/encodefirst', methods=['GET', 'POST'])
def upload_file_encode_first():
    if(os.path.exists("base.JPG")):
            os.remove("base.JPG")
    with open("base.JPG", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
    urldict = {"url": '/base.JPG'}
    return jsonify(urldict)

@app.route('/encodesecond', methods=['GET', 'POST'])
def upload_file_encode_second():
    if(os.path.exists("hidden.JPG")):
            os.remove("hidden.JPG")
    removeTempFiles(encoded_images)
    with open("hidden.JPG", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
    while(not os.path.exists("base.JPG")):
        sleep(1)
    if(os.path.exists("base.JPG")):
        base = skio.imread("base.JPG")
        hidden = skio.imread("hidden.JPG")
        filename='encoded_image' + id_generator()
        sf.saveEncoded(base, hidden, filename)
        urldict = {"url": filename + ".png"}
        if(os.path.exists("hidden.JPG")):
            os.remove("hidden.JPG")
        if(os.path.exists("base.JPG")):
            os.remove("base.JPG")
        return jsonify(urldict)
    else:
        return jsonify({"url": ''})

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run()
