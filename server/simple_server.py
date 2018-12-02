from flask import Flask, flash, request, send_from_directory, redirect, url_for
import stego_functions as sf
import skimage.io as skio

app = Flask(__name__)

DECODED_FOLDER='.'
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {
        "encode": ['png', 'jpg', 'jpeg'],
        "decode": ['png']
        }    

def allowed_file(filename, version):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS[version]

@app.route('/decode', methods=['GET', 'POST'])
def upload_file_decode():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
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

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DECODED_FOLDER'],
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

    sess.init_app(app)

    app.debug = True
    app.run()
