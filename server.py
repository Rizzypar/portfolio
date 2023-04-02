from flask import Flask, render_template, request

app = Flask(__name__,template_folder='/Web/template/')

@app.route("/")
def my_home():
    return render_template('index.html')

