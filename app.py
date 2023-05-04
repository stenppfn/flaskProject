from flask import Flask, render_template
from config import config

app = Flask(__name__)
app.config.from_object(config['development'])
config['development'].init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('base.html')

@app.route('/button')
def button():  # put application's code here
    return render_template('button.html')

if __name__ == '__main__':
    app.run(debug=True)
