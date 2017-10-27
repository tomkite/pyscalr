# Python API for Scalr

<em>This repo was based on [scalr-tutorials/apiv2-examples](https://github.com/scalr-tutorials/apiv2-examples.git). Only python folder was copied to make it python specific.</em>

## Below is the original README.md content:

Scalr APIv2 Python sample
=========================

This directory contains Python code samples for the Scalr API. An actual API client is contained within [`./api`](./api).

Using this sample
-----------------

  1. (Optional) Create a Python virtual environment to avoid installing dependencies system-wide
  2. Install the dependencies: `pip install requirements.txt` (you might need to `sudo` if you are installing system-wide).
  3. Create a credentials file: copy `credentials-sample.json` to `creds.json` and update the values there.
  4. Run the sample code: `python main.py creds.json list` and `python main.py creds.json create`. See below for more information.
 
 
Scenarii
--------

Two sample scenarii are included:

  + `list` calls the Scalr API to list Roles, Images, Role Categories, and OSes.
  + `create` creates an Image and a Role, associates the Image with the Role, and then cleans up by undoing everything
    it did.
    
You can find the code for those samples under [`scenarii`](./scenarii).
