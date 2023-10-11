from flask import Flask, render_template, send_file

app = Flask(__name__, static_folder="build/static", template_folder="build")


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/logo.png")
def logo():
    return send_file('build/static/logo.png')


print('Running EUTCHA Serving Application')


app.run(host="0.0.0.0", port=5001, debug=True)