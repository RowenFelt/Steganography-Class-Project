from flask import Flask, flash, request, send_from_directory, redirect, url_for, jsonify
import stego_functions as sf
import skimage.io as skio
import png
import flask_cors
import os
from decorator import crossdomain

app = Flask(__name__)
flask_cors.CORS(app)

DECODED_FOLDER='.'
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {
        "encode": ['png', 'jpg', 'jpeg'],
        "decode": ['png']
        }

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

def removeTempFiles():
    for i in ["decoded.png", "uploaded-for-decoding.png"]:
        if os.path.exists(i):
            os.remove(i)

def allowed_file(filename, version):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[version]

@app.route('/decode', methods=['POST'])
def upload_file_decode():
    removeTempFiles()
    with open("uploaded-for-decoding.png", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
        base = skio.imread('uploaded-for-decoding.png')
    sf.saveDecoded(base, "decoded")
    imageurl = "/decoded.png"
    urldict = {"url": imageurl}
    return jsonify(urldict)

@app.route('/<filename>')
@crossdomain(origin='*')
def uploaded_file(filename):
    return send_from_directory('.',
                               filename)
@app.route('/encodefirst', methods=['GET', 'POST'])
def upload_file_encode_first():
    if(os.path.exists("base.png"):
            os.remove("base.png")
    with open("base.png", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
        base = skio.imread('base.png')
    urldit = {"url": '/base.png'}
    return jsonify(urldict)

@app.route('/encodesecond', methods=['GET', 'POST'])
def upload_file_encode_first():
    if(os.path.exists("hidden.png"):
            os.remove("hidden.png")
    with open("hidden.png", "wb") as binary_file:
        num_bytes_written = binary_file.write(request.data)
        base = skio.imread('hidden.png')
    if(os.path.exists("base.png"):
        base = skio.imread("base.png")
        hidden = skio.imread("hidden.png")
        sf.saveEncoded(base, hidden, 'encoded_image.png')
    urldit = {"url": '/encoded_image.png'}
    return jsonify(urldict)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run()
