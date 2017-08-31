from flask import Flask, request, redirect, session
from views import Upload, upload_nonadmin, files_na, serve_na, files_a, serve_a
from auth import login_required, login, logout, register
from settings import allowed_file, video_type, song_type, pdf_type, docs_type, image_type
from pdf_reader import pdf_reader

app = Flask(__name__ , static_url_path='/static')
app.secret_key = "weubfyiwobyfuw;elfuvyw;vy56243i38v8;evwf8fvywelu"

@app.route('/', methods=['GET', 'POST'])
@login_required
def hello():
    if 'is_admin' in session:
    	if (request.method == "POST"):
    	    return Upload("home/pandey/")
    	else:
            return files_a()
    else:
        if request.method == "POST":
    	    return upload_nonadmin()
        else:
            return files_na()

@app.route('/<path:filename>', methods=['GET', 'POST'])
@login_required
def download(filename):
    if 'is_admin' in session:
    	if (request.method == "POST"):
    	    return Upload(filename)
    	else:
    	    return serve_a(filename)
    else:
        if request.method == "POST":
    	    return upload_nonadmin()
        else:
            return serve_na(filename)

@app.route('/pdf', methods=[ 'POST'])
@login_required
def read_pdf():
    name = str(request.form['name'])
    page = str(request.form['page'])
    return pdf_reader(name, page)

@app.route('/register', methods=['GET', 'POST'])
def do_register():
    return register()

@app.route('/login', methods=['GET', 'POST'])
def do_login():
    return login()

@app.route('/logout')
@login_required
def do_logout():
	return logout()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, processes=3, debug=True)
