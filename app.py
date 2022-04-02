from flask import Flask, render_template, request, send_file, send_from_directory
from encoder import compression
from decoder import Decompression
from file_list import get_file_list, remove_file

import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    fileList = get_file_list()
    return render_template('index.html', files = fileList)

@app.route('/compress', methods=['POST'])
def compress():
    # -- uploaded file setup
    file = request.files['fileInput']
    file_path = "./upload/" + file.filename
    file.save(file_path)

    # -- compression setup
    get_name = file.filename.split(".")[0]
    compression(file_path, get_name)

    fileList = get_file_list()
    return render_template('index.html', files = fileList)

@app.route('/uncompress/<name>', methods=['GET'])
def uncompress(name):
    # -- get compressed file path
    file_path = "./compressed/" + name

    # -- decompression setup
    new_path = Decompression(file_path, name)

    return send_file(new_path, as_attachment=True)
    # return send_from_directory(directory=new_path, filename = "READ ME.lzw_decoded.txt", path = new_path)
    # return render_template('index.html', file = fileList)

@app.route('/delete/<name>')
def my_view_func(name):
    remove_file(name)
    
    fileList = get_file_list()
    return render_template('index.html', files = fileList)

if __name__ == '__main__':
    app.run(port=3000, debug=True)