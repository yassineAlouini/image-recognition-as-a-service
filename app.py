from flask import Flask

# from image_classification import ImageClassifier

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello classification world!'


if __name__ == '__main__':
    app.run()
