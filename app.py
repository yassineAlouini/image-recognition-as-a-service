import os

from flask import Flask

import keras.preprocessing.image as image_utils
from image_classification import ImageClassifier

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello classification world!'


@app.route('/test')
def test():
    """ Test that the image recognition model is working using a local image.
    """
    test_path = os.path.join(os.path.dirname(
        os.path.realpath(__file__)), 'data', 'cat_awake.JPG')
    print(test_path)
    img_clf = ImageClassifier()
    top_label = img_clf.get_top_label(test_path)
    return top_label


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    HOST = '0.0.0.0'
    app.run(host=HOST, port=PORT)
