# Inspired from this blog post:
# http://www.pyimagesearch.com/2016/08/10/imagenet-classification-with-python-and-keras/

import argparse

import numpy as np

import cv2
import keras.preprocessing.image as image_utils
from keras.applications.imagenet_utils import (decode_predictions,
                                               preprocess_input)
from keras.applications.resnet50 import ResNet50

TEXT_COLOR = (255, 255, 255)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True,
                        help="path to the input image")
    args = vars(parser.parse_args())
    orig = cv2.imread(args["image"])
    # Load and process the image
    image = image_utils.load_img(args["image"], target_size=(224, 224))
    image = image_utils.img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    # Load the model and make predictions
    model = ResNet50()
    preds = model.predict(image)
    print('The top 5 labels are: (in descending order)')
    for inID, label, score in decode_predictions(preds)[0]:
        print(label, score)
    top_label = decode_predictions(preds)[0][0][1]
    cv2.putText(orig, "Top label: {}".format(top_label), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, TEXT_COLOR, 2)
    cv2.imshow("Classification", orig)
    cv2.waitKey(0)
