import os

from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename

import keras.preprocessing.image as image_utils
from image_classification import ImageClassifier

DATA_FOLDER_PATH = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'data')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = DATA_FOLDER_PATH
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
img_clf = ImageClassifier()


@app.route('/upload', methods=['GET', 'POST'])
def upload_img():
    """ Upload an image and redirect to the recognition URL.
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
    """ Use the image classification class to recognize the top label on the
    uploaded image.
    """
    try:
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        top_label = img_clf.get_top_label(img_path)
        return f"The top label for the  uploaded image is: {top_label}"
    except FileNotFoundError:
        return "The requested image wasn't found. :("


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    HOST = '0.0.0.0'
    app.run(host=HOST, port=PORT)
