from flask import Flask, render_template, request, url_for, redirect, flash
import transcribe

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        transcribe.main()
        return "zero"
    else:
        return render_template("template1.html")







