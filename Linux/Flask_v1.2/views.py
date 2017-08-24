from flask import Flask, render_template, request, send_from_directory, redirect, current_app,  session
from glob import glob, re, os
from werkzeug import secure_filename
from settings import allowed_file, video_type, song_type, pdf_type, docs_type, image_type

app = Flask(__name__)
app.config['DOWNLOAD_FOLDER'] = 'Uploads/'
app.config['UPLOAD_FOLDER'] = '/'

def Upload(foldername):
    uploaded_files = request.files.getlist("file[]")
    name = foldername.rsplit("/",1)[0]
    app.config['DOWNLOAD_FOLDER'] = '/'+ foldername
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        if filename and allowed_file(filename):
            file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    return redirect('/'+foldername)

def upload_nonadmin():
    uploaded_files = request.files.getlist("file[]")
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        if filename and allowed_file(filename):
            file.save(os.path.join(app.config['DOWNLOAD_FOLDER'], filename))
    return redirect('/')

def files_na():
    names = glob("Shares/*.*")
    listing = []
    for name in names:
        name = re.split('/',name)[1]
        listing.append(name)
    return render_template('index1.html', names = listing)

def serve_na(Filename):
    app.config['UPLOAD_FOLDER'] = "Shares/"
    uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    ip = request.remote_addr
    log = open('log.txt','a')
    log.write("Filename = " + Filename + ", IP-Address = " + ip + '\n')
    log.close()
    return send_from_directory(directory=uploads, filename=Filename)

def files_a():
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
    return render_template('index.html', names = names, folder_name = interface, filetype = filetype , user = session['user'])

def serve_a(filename):
    check = re.split('/', filename)
    if (check[0] == u'home'):
	if (os.path.isfile("/"+filename)):
	    ip = request.remote_addr
	    log = open('log.txt','a')
	    log.write("Filename = " + filename + ", Username = " + session['user'] + ", IP-Address = " + ip + '\n')
	    log.close()
	    if filename and allowed_file(filename):
		uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
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
		if len(folder_name) > 22:
		    folder_name = folder_name[:22].lower()
		interface.append(folder_name)
		if (os.path.isdir("/"+filename)):
		    filetype.append(0)
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
	return ("Not Allowed")
