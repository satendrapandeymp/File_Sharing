from flask import Flask, render_template, request, jsonify, current_app, send_from_directory, redirect
import os, urllib2, re
from glob import glob
from werkzeug import secure_filename

app = Flask(__name__ , static_url_path='/static')

app.config['UPLOAD_FOLDER'] = 'Shares/'
app.config['DOWNLOAD_FOLDER'] = 'Uploads/'

@app.route('/')
def hello():
	names = glob("Shares/*.*")
	listing = []
	for name in names:
		name = re.split('/',name)[1]
		listing.append(name)
	return render_template('index.html', names = listing)

@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
	if (request.method == "POST"):
	    uploaded_files = request.files.getlist("file[]")
	    for file in uploaded_files:
		    filename = secure_filename(file.filename)
		    file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
	    return redirect('/')	
		
	else:
		uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
		return send_from_directory(directory=uploads, filename=filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, processes=3, debug=True)
