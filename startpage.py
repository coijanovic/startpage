from flask import Flask, render_template, request, redirect, url_for
import os.path
import yaml
import time

if os.path.exists('config.yaml'):
    configfile = 'config.yaml'
else:
    configfile = 'defaultconfig.yaml'

with open(configfile, 'r') as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as exc:
        print(exc)

app = Flask(__name__)

@app.route('/')
def index():
    r = "Hi Christoph"
    return r

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)
