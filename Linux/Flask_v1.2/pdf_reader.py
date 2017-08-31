from PyPDF2 import PdfFileReader
from gtts import gTTS
import os, pyttsx, time
from flask import Flask, render_template, request, jsonify

def pdf_reader(name, page):
    infile = PdfFileReader(name, 'rb')
    page = int(page)
    reader_temp = infile.getPage(page)
    data = reader_temp.extractText()
    tts = gTTS(text=data , lang='en')
    name = "static/temp/" + str(page) + ".mp3"
    tts.save(name)
    return jsonify({'status':'OK','answer':name})
