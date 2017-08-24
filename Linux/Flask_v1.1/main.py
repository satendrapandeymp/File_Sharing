from flask import Flask, render_template, request, jsonify, current_app, send_from_directory, redirect
import os, urllib2, re
from glob import glob
from werkzeug import secure_filename
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__ , static_url_path='/static')

app.config['UPLOAD_FOLDER'] = '/'
app.config['DOWNLOAD_FOLDER'] = 'Uploads/'

app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'mp3', 'm4a' , 'mp4', 'webm', 'avi', 'pdf', 'txt', 'odf', 'pptx', 'xls', 'doc', 'docx'])

app.config['VIDEO_EXTENSIONS'] = set([ 'mp4', 'webm', 'avi', 'mkv'])

app.config['AUDIO_EXTENSIONS'] = set([ 'm4a' , 'mp3'])

app.config['DOCS_EXTENSIONS'] = set([ 'odf', 'pptx', 'xls', 'doc', 'docx', 'txt'])

app.config['PDF_EXTENSIONS'] = set([ 'pdf'])

app.config['IMAGE_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'ico'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def video_type(filename):
    exten = filename.split('.')
    extention = exten[len(exten)-1]
    return extention in app.config['VIDEO_EXTENSIONS']

def song_type(filename):
    exten = filename.split('.')
    extention = exten[len(exten)-1]
    return extention in app.config['AUDIO_EXTENSIONS']

def image_type(filename):
    exten = filename.split('.')
    extention = exten[len(exten)-1]
    return extention in app.config['IMAGE_EXTENSIONS']

def pdf_type(filename):
    exten = filename.split('.')
    extention = exten[len(exten)-1]
    return extention in app.config['PDF_EXTENSIONS']

def docs_type(filename):
    exten = filename.split('.')
    extention = exten[len(exten)-1]
    return extention in app.config['DOCS_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def hello():
    if (request.method == "POST"):
	uploaded_files = request.files.getlist("file[]")
	app.config['DOWNLOAD_FOLDER'] = '/home/pandey'
	for file in uploaded_files:
	    filenames = secure_filename(file.filename)
	    if filenames and allowed_file(filenames):
		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filenames))
	return redirect('/')    
    # if user is admin:
    names = glob("/home/*")
    interface = []
    filetype = []
    for filename in names:
        folder = filename.split("/")
        a = len(folder)
        folder_name = folder[a-1]
        interface.append(folder_name)

        if (os.path.isdir("/"+filename)):
            filetype.append(0)
        else:
            # for image -- 1, songs --2, videos  -- 3, pdf -- 4, txt -- 5, world files -- 6
            if filename and image_type(filename):
                filetype.append(1)
            elif filename and song_type(filename):
                filetype.append(2)
            elif filename and video_type(filename):
                filetype.append(3)
            elif filename and pdf_type(filename):
                filetype.append(4)
            elif filename and docs_type(filename):
                filetype.append(5)
            else:
                filetype.append(6)
    return render_template('index.html', names = names, folder_name = interface, filetype = filetype)


@app.route('/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    if (request.method == "POST"):
	uploaded_files = request.files.getlist("file[]")
	app.config['DOWNLOAD_FOLDER'] = '/'+ filename
	for file in uploaded_files:
	    filenames = secure_filename(file.filename)
	    if filenames and allowed_file(filenames):
		file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filenames))
	return redirect('/'+filename)

    # if user is admin:
    else:
    	check = re.split('/', filename)
    	if (check[0] == u'home'):
    		if (os.path.isfile("/"+filename)):
    			if filename and allowed_file(filename):
    				uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    				log = open('log.txt','a')
    				log.write(filename + '\n')
    				log.close()
    				return send_from_directory(directory=uploads, filename=filename)
    			else:
    				return "Not allowed"

    		else:
		    filename = filename.replace('[','[[]')
		    abs_path = "/" + str(filename) + '/*'
		    names = glob(abs_path)
		    filetype = []
		    interface = []
		    for filename in names:
			folder = filename.split("/")
			a = len(folder)
			folder_name = folder[a-1]
			interface.append(folder_name)
			if (os.path.isdir("/"+filename)):
			    filetype.append(0)
			# for image -- 1, songs --2, videos  -- 3, pdf -- 4, txt -- 5, world files -- 6
			elif filename and image_type(filename):
			    filetype.append(1)
			elif filename and song_type(filename):
			    filetype.append(2)
			elif filename and video_type(filename):
			    filetype.append(3)
			elif filename and pdf_type(filename):
			    filetype.append(4)
			elif filename and docs_type(filename):
			    filetype.append(5)
			else:
			    filetype.append(6)
		    return render_template('index.html', names = names, folder_name = interface, filetype = filetype)
    	else:
	    return ("Fuck You")
    # for non admin
        #uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
		#return send_from_directory(directory=uploads, filename=filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, processes=3, debug=True)
