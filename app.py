from flask import flask, render_template
app=flask(__name__)

@app.route("/")
def hello_world():
    return ""
