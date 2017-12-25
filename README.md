# Image recognition as a service

## Description

This is the accompanying repository for the fourth installment in the Keras
blog post series. You can find it [here](https://dsotb.quora.com)

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

The deployment process is explained in the blog post, in the
**Deploying to Heroku** section.
