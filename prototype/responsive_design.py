import os
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

def optimizeDesign():
    if os.name == 'nt':
        return 'windows.css'
    elif os.name == 'posix':
        return 'unix.css'
    else:
        return 'default.css'

@app.context_processor
def inject_css():
    return dict(css_file=optimizeDesign())

if __name__ == '__main__':
    app.run(debug=True)