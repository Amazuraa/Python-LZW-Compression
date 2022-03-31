from flask import Flask, render_template, request
from encoder import compression

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def uploaded():
    # -- uploaded file setup
    file = request.files['fileInput']
    file_path = "./upload/" + file.filename
    file.save(file_path)

    # -- compression setup
    compression(file_path)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=3000, debug=True)