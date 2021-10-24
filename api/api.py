import time
from flask import Flask
import transcribe

app = Flask(__name__)

@app.route('/text')
def get_current_text():
    return {'time': time.time()}

data1 = { 
  'values': [
    {
      "country": "AD",
      "hot dog": 1,
      "hot dogColor": "hsl(226, 70%, 50%)"
    },
    {
      "country": "AE",
      "hot dog": 2,
      "hot dogColor": "hsl(130, 70%, 50%)"
    },
    {
      "country": "AF",
      "hot dog": 3,
      "hot dogColor": "hsl(304, 70%, 50%)"
    },
    {
      "country": "AG",
      "hot dog": 4,
      "hot dogColor": "hsl(225, 70%, 50%)"
    },
    {
      "country": "AI",
      "hot dog": 5,
      "hot dogColor": "hsl(161, 70%, 50%)"
    },
    {
      "country": "AL",
      "hot dog": 6,
      "hot dogColor": "hsl(93, 70%, 50%)"
    },
    {
      "country": "AM",
      "hot dog": 7,
      "hot dogColor": "hsl(119, 70%, 50%)"
    }
  ]
}

@app.route('/data')
def get_data():
  return data1



@app.route('/transcribe')
def transcribe_audio():
    transcribe.main()
    
    with open('text-linebyline.txt', 'r') as f:
        lines = f.readLines()
    return lines
  