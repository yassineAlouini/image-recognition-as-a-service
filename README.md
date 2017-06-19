# Image recognition as a service

## Description

This is the accompanying repo for the fourth installment in the Keras
blog post series.

## Installation

Run: `conda env create -f environment.yml`

Once you have created the virtualenv,
don't forget to activate it: `source activate img-reco`.


## Testing
To test that the classification module is working, you can run:

`python image_classification.py -i data/cat_sleeping.JPG`.

## Deploying
https://devcenter.heroku.com/articles/getting-started-with-python#introduction

To add Conda support, run the following command:

`heroku config:add BUILDPACK_URL=https://github.com/kennethreitz/conda-buildpack.git`

For more detils, check the following [repo](https://github.com/kennethreitz/conda-buildpack).
