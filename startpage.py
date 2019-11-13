from flask import Flask, render_template, request, redirect, url_for
import os.path
import yaml
import json
import wget
import time
from datetime import datetime

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
    # 2. Date
    td = "Today is {d}".format(d=datetime.now().strftime("%A, the %-dth of %B %Y"))
    # 3. Weather
    url = "https://api.openweathermap.org/data/2.5/weather?q={l}&id=4737316&units={u}&appid=e5b292ae2f9dae5f29e11499c2d82ece".format(l=config['location'],u=config['units'])
    f = wget.download(url, out="weather.json")
    weather = json.loads(open(f).read())
    w = "Outside, it's {t} °C and {h}".format(t=round(weather['main']['temp']), h=weather['weather'][0]['description'])
    data = [td, w]
    return render_template('index.html', data=data);

if __name__ == '__main__':
    app.run(debug=True,host=config['hostip'],port=config['hostport'])
