from flask import Flask, render_template, request, send_file, send_from_directory
from encoder import compression
from decoder import Decompression
from file_list import get_file_list, remove_file, get_file_size
from model import Database

import os

db = Database()
app = Flask(__name__)
app.secret_key = "lorem_Ipsums"


@app.route('/', methods=['GET'])
def homepage():
    fileList = db.read(None)
    return render_template('index.html', files = fileList)

@app.route('/compress', methods=['POST'])
def compress():
    # -- uploaded file setup
    file = request.files['fileInput']
    file_path = "./upload/" + file.filename
    file.save(file_path)

    # -- compression setup
    get_name = file.filename.split(".")[0]
    
    try:
        compression(file_path, get_name)
    finally:
        print("X")
        dat = {
            'file_name' : get_name + ".lzw",
            'file_size' : get_file_size(get_name + ".lzw")
        }
        db.insert(dat)

    fileList = db.read(None)
    return render_template('index.html', files = fileList)

@app.route('/uncompress/<name>', methods=['GET'])
def uncompress(name):
    # -- get compressed file path
    file_path = "./compressed/" + name

    # -- decompression setup
    new_path = Decompression(file_path, name)

    return send_file(new_path, as_attachment=True)

@app.route('/delete/<name>')
def my_view_func(name):
    remove_file(name)
    db.delete(name)

    fileList = db.read(None)
    return render_template('index.html', files = fileList)

if __name__ == '__main__':
    app.run(port=3000, debug=True)