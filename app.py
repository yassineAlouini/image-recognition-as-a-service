import os

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

import keras.preprocessing.image as image_utils
from image_classification import ImageClassifier

app = Flask(__name__)
DATA_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'data')
app.config['UPLOAD_FOLDER'] = DATA_FOLDER_PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
img_clf = ImageClassifier()


@app.route('/upload', methods=['GET', 'POST'])
def upload_and_rec_img():
    """ Upload and recognize an image.
    """
    # Inspired from this:
    # http://flask.pocoo.org/docs/0.12/patterns/fileuploads/#uploading-files
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(img_path)
        top_label = img_clf.get_top_label(img_path)
        return redirect(url_for('rec_img', filename=filename))
    else:
        return render_template('upload.html')


@app.route('/upload/<filename>')
def rec_img(filename):
    try:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        top_label = img_clf.get_top_label(img_path)
        # Remove the image to avoid flooding the disk
        os.remove(img_path)
        return f"The top label for the  uploaded image is: {top_label}"
    except FileNotFoundError:
        return "The requested image wasn't found. :("


@app.route('/')
def home():
    return 'Welcome to your image recognition API!'


@app.route('/test')
def test():
    """ Test that the image recognition model is working using a local image.
    """
    test_path = os.path.join(DATA_FOLDER_PATH, 'cat_awake.JPG')
    top_label = img_clf.get_top_label(test_path)
    return f"The top label for the test image is: {top_label}"


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    HOST = '0.0.0.0'
    app.run(host=HOST, port=PORT)
