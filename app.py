from flask import Flask, render_template, request
from encoder import compression
from file_list import get_file_list, remove_file

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

@app.route('/uncompress', methods=['GET'])
def uncompress():
    # -- get compressed file path

    # -- decompression setup

    return render_template('index.html')

@app.route('/delete/<name>')
def my_view_func(name):
    remove_file(name)
    
    fileList = get_file_list()
    return render_template('index.html', files = fileList)

if __name__ == '__main__':
    app.run(port=3000, debug=True)