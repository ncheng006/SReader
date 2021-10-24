import time
from flask import Flask
import transcribe
import readability_index

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


def extract(file_path="text-linebyline.txt"):
    with open(file_path, 'r') as f:
        lines = f.read()
    return lines
