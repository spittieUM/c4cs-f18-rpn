from flask import Flask, url_for
from flask import request
from flask import render_template
import rpn
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def addProduct():
    if request.method == 'POST':
        eq = request.form['eq']

        return render_template('index.html', val=rpn.calculate(eq))

    else:
        return render_template('index.html', val="")

        
    
with app.test_request_context():
    url_for('static', filename='bootstrap.min.css')
    url_for('static', filename='jquery-1.11.3.min.js')
    url_for('static', filename='bootstrap.min.js')

if __name__ == "__main__":
    app.run()