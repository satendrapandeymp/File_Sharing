from flask import Flask
app = Flask(__name__)

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
