from flask import Flask

# from image_classification import ImageClassifier

app = Flask(__name__)
PORT = 33507
HOST = '0.0.0.0'


@app.route('/')
def home():
    return 'Hello classification world!'


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
