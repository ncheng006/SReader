import time
from flask import Flask
import transcribe
import readability_index

app = Flask(__name__)


@app.route('/text')
def get_current_text():
    return {'time': time.time()}


data1 = {
    "id": "norway",
    "color": "hsl(83, 70%, 50%)",
    "data": [
      {
        "x": "plane",
        "y": 72
      },
      {
        "x": "helicopter",
        "y": 280
      },
      {
        "x": "boat",
        "y": 55
      },
      {
        "x": "train",
        "y": 140
      },
      {
        "x": "subway",
        "y": 169
      },
      {
        "x": "bus",
        "y": 146
      },
      {
        "x": "car",
        "y": 69
      },
      {
        "x": "moto",
        "y": 226
      },
      {
        "x": "bicycle",
        "y": 224
      },
      {
        "x": "horse",
        "y": 236
      },
      {
        "x": "skateboard",
        "y": 210
      },
      {
        "x": "others",
        "y": 263
      }
    ]
  }


@app.route('/data')
def get_data():
    return data1


@app.route('/transcribe')
def start_transcribing():
    """
        this starts transcribing for up to (60) seconds
        note: 60 seconds is arbitrary
    """
    transcribe.main()


@app.route('/read')
def read_text_from_audio():
    return {"lines": extract()}


@app.route('/read_obj_stuff')
def read_obj_data():
    text = extract('file2.txt')
    
    # text is the list of json objects, work on extracting the timestamps
    # daniel: start here


@app.route('/dalechall')
def get_dale_chall():
    # this is dale chall readability score
    text = extract()
    score = readability_index.dale_chall_readability_score(text)
    return score


@app.route('/smogindex')
def get_smog_index():
    text = extract()
    score = readability_index.smog_index(text)
    return score


@app.route('/gunningease')
def get_gunning_ease():
    text = extract()
    score = readability_index.gunning_fog(text)
    return score


@app.route('/flesch')
def get_flesch():
    text = extract()
    score = readability_index.flesch_reading_ease(text)
    return score

metrics = [{
    "id": "dalechall",
    "color": "hsl(83, 70%, 50%)",
    "data": []
  },{
    "id": "smogindex",
    "color": "hsl(335, 70%, 50%)",
    "data": []
  },{
    "id": "gunningease",
    "color": "hsl(55, 70%, 50%)",
    "data": []
  },{
    "id": "flesch",
    "color": "hsl(23, 70%, 50%)",
    "data": []
  }]
timestep = 0

@app.route('/all_metrics')
def get_all_metrics():
    global metrics
    global timestep
    getMetric = [get_dale_chall, get_smog_index, get_gunning_ease, get_flesch]
    for i in range(len(metrics)):
        data = metrics[i]['data']
        data.append({'x': timestep, 'y': getMetric[i]()})
        metrics[i]['data'] = data
    timestep += 1


def extract(file_path="text-linebyline.txt"):
    with open(file_path, 'r') as f:
        lines = f.read()
    return lines
