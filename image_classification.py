import argparse

import numpy as np

import cv2
import keras.preprocessing.image as image_utils
from keras.applications.imagenet_utils import (decode_predictions,
                                               preprocess_input)
from keras.applications.resnet50 import ResNet50

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    args = vars(ap.parse_args())
    # load the original image via OpenCV so we can draw on it and display
    # it to our screen later
    orig = cv2.imread(args["image"])
    image = image_utils.load_img(args["image"], target_size=(224, 224))
    image = image_utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    model = ResNet50()
    preds = model.predict(image)
    for inID, label, score in decode_predictions(preds)[0]:
        print(label, score)
