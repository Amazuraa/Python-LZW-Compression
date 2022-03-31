from flask import Flask, render_template, request
from encoder import compression

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    # -- uploaded file setup
    file = request.files['fileInput']
    file_path = "./upload/" + file.filename
    file.save(file_path)

    # -- compression setup
    get_name = file.filename.split(".")[0]
    compression(file_path, get_name)

    return render_template('index.html')

@app.route('/uncompress', methods=['GET'])
def uncompress():
    # -- get compressed file path

    # -- decompression setup

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)