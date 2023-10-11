from flask import Flask, render_template

app = Flask(__name__, static_folder="build/static", template_folder="build")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/logo.png")
def logo():
    return Flask.send_static_file (filename= "logo.png")

print('Starting Flask!')

app.debug=True
app.run(host= "0.0.0.0", port=5001)
