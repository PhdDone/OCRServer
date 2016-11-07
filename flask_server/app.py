import os
import logging
from logging import Formatter, FileHandler
from flask import Flask, request, jsonify, render_template, send_from_directory

from ocr import process_image, process_image_file_jpg, process_image_file_png

app = Flask(__name__)
_VERSION = 1  # API version

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def main():
    return render_template('index.html')

'''
def ocr2():
    try:
        url = request.json['image_url']
        if 'jpg' in url:
            output = process_image(url)
            return jsonify({"output": output})
        else:
            return jsonify({"error": "only .jpg files, please"})
    except:
        return jsonify(
            {"error": "Did you mean to send: {'image_url': 'some_jpeg_url'}"}
        )
'''

@app.route('/your_method_name', methods=['POST'])
def addRegion():
    print("I got it!")
    print(request.form['projectFilepath'])
    return jsonify({"error": "only .jpg files, please"})

@app.route('/ocr/<filename>')
def send_image(filename):
    print("%%%%%%%%%%%%%")
    print filename
    path = os.path.join(APP_ROOT, 'images/') #use full path
    return send_from_directory(path, filename)

#@app.route('/ocr', methods=['POST'])
@app.route('/v{}/ocr'.format(_VERSION), methods=["POST"])
def ocr():
    print("###############")
    target = os.path.join(APP_ROOT, 'images/')
    print("###############")
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    upload = request.files['file']
    print(upload)
    #for upload in request.files.getlist("file"):
    print(upload)
    print("{} is the file name".format(upload.filename))
    filename = upload.filename
    # This is to verify files are supported
    ext = os.path.splitext(filename)[1]
    print ext
    if (ext == ".jpg") or (ext == ".png"):
        print("File supported moving on...")
    else:
        render_template("Error.html", message="Files uploaded are not supported...")
    destination = "/".join([target, filename])
    print("Accept incoming file:", filename)
    print("Save it to:", destination)
    upload.save(destination)
    url = destination
    if 'jpg' in url:
        output = process_image_file_jpg(url)
        return jsonify({"filename": filename, "output": output})
    else:
        if 'png' in url:
            output = process_image_file_png(url)
            return jsonify({"filename": filename, "output": output})
        return jsonify({"error": "only .jpg and .png files, please"})

@app.errorhandler(500)
def internal_error(error):
    print str(error)  # ghetto logging


@app.errorhandler(404)
def not_found_error(error):
    print str(error)

if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: \
            %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print("$$")
    app.debug = False
    app.run(host='0.0.0.0', port=port)
