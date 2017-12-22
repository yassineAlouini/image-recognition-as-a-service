# Image recognition as a service

## Description

This is the accompanying repository for the fourth installment in the Keras
blog post series.

## Installation

Run: `conda env create -f environment.yml`

Once you have created the virtualenv,
don't forget to activate it: `source activate img-reco`. Notice that
the installation has only been tested on Ubuntu 16.04. Thus it can fail
on your particular setup.


## Testing

To test that the classification module is working, you can run:

`python image_classification.py -i data/cat_sleeping.JPG`.

## Deploying

https://devcenter.heroku.com/articles/getting-started-with-python#introduction

To add Conda support, run the following command:

`heroku buildpacks:set https://github.com/trib3/conda-buildpack.git -a <app_name>`


For more detils, check the following [repo](https://github.com/trib3/conda-buildpack).
