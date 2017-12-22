# Inspired from this blog post:
# http://www.pyimagesearch.com/2016/08/10/imagenet-classification-with-python-and-keras/


import numpy as np

import keras.preprocessing.image as image_utils
from keras.applications.imagenet_utils import (decode_predictions,
                                               preprocess_input)
from keras.applications.resnet50 import ResNet50
from utils import logger

TEXT_COLOR = (255, 255, 255)
IMG_SIZE = (224, 224)
TEXT_POSITION = (10, 30)


class ImageClassifier(object):

    def __init__(self):
        self.model = ResNet50()

    def get_top_label(self, img_path):
        """Given an image path, return the top detected label
        using a ResNet50 model.
        """
        image = image_utils.load_img(img_path, target_size=IMG_SIZE)
        image = image_utils.img_to_array(image)
        image = np.expand_dims(image, axis=0)
        image = preprocess_input(image)
        preds = self.model.predict(image)
        top_label = decode_predictions(preds)[0][0][1]
        return top_label


def classifier_cli():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True,
                        help="path to the input image")
    args = vars(parser.parse_args())
    img_clf = ImageClassifier()
    top_label = img_clf.get_top_label(args["image"])
    logger.info(top_label)

if __name__ == '__main__':
    classifier_cli()
