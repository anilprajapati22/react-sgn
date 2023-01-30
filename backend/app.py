import os
import urllib.request
from flask import Flask, request, redirect, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png',  'json', 'jpg', 'jpeg', 'gif'])



UPLOAD_FOLDER = '/home/sgnons/upoaded_file'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

app = Flask(__name__)
# Members API Route
CORS(app)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/file-upload', methods=['POST'])
def upload_file():
	# check if the post request has the file part
	if 'file' not in request.files:
		resp = jsonify({'message' : 'No file part in the request'})
		resp.status_code = 400
		return resp
	file = request.files['file']
	if file.filename == '':
		resp = jsonify({'message' : 'No file selected for uploading'})
		resp.status_code = 400
		return resp
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(UPLOAD_FOLDER, filename))
		resp = jsonify({'message' : 'File successfully uploaded'})
		resp.status_code = 201
		return resp
	else:
		resp = jsonify({'message' : 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
		resp.status_code = 400
		return resp

@app.route("/sgnons")
def members () :
    return {"sgnons" : ['sgnonsjkhjbmam',"jcsjkbjrmjhdjsbjjbjamjomjsmjsmjlmjsmjsmjlmjkbjgbjjbjdjdjmpjgdjrbjspb"]}
if __name__ == "__main__":
    app.run(debug=True)
