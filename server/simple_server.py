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
    #if request.method == 'POST':
    #    # check if the post request has the file part
    #    if 'file' not in request.files:
    #        flash('No file part')
    #        return redirect(request.url)
    #    file = request.files['file']
    #    # if user does not select file, browser also
    #    # submit an empty part without filename
    #    if file.filename == '':
    #        flash('No selected file')
    #        return redirect(request.url)
    #    if file and allowed_file(file.filename, "decode"):
    #        filename = secure_filename(file.filename)
    #        filetrunct = filename.rsplit('.', 1)[0]
    #        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #        base = skio.imread(filename)
    #        decode_filename = filetrunct + "decoded" + ".png"  
    #        sf.saveDecoded(base, decode_filename)
    #        return redirect(url_for('uploaded_file',
    #                                filename=decodedfilename))
    base = skio.imread('uploaded-for-decoding.png')
    sf.saveDecoded(base, "decoded")
    #return redirect(url_for('uploaded_file',filename="decoded.png"))
    imageurl = "/decoded.png"
    urldict = {"url": imageurl}
    #listdict =([]).append(urldict)
    #jsonStr = json.dumps( 
    return jsonify(urldict)

@app.route('/<filename>')
@crossdomain(origin='*')
def uploaded_file(filename):
    return send_from_directory('.',
                               filename)
@app.route('/encode', methods=['GET', 'POST'])
def upload_file_encode():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        uploaded_files = request.files.getlist("file[]")
        print(uploaded_files)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename, "decode"):
            filename = secure_filename(file.filename)
            filetrunct = filename.rsplit('.', 1)[0]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            base = skio.imread(filename)
            decode_filename = filetrunct + "decoded" + ".png"  
            sf.saveDecoded(base, decode_filename)
            return redirect(url_for('uploaded_file',
                                    filename=decodedfilename))

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'


    app.debug = True
    app.run()
