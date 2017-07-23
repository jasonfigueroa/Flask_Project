from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    weather = {
        'January': {'min': 50, 'max': 71, 'rain': 2.76},
        'February': {'min': 53, 'max': 73, 'rain': 2.83},
        'March': {'min': 57, 'max': 77, 'rain': 3.78},
        'April': {'min': 62, 'max': 82, 'rain': 2.48},
        'May': {'min': 68, 'max': 88, 'rain': 3.31},
        'June': {'min': 73, 'max': 91, 'rain': 8.74},
        'July': {'min': 76, 'max': 92, 'rain': 7.09},
        'August': {'min': 76, 'max': 92, 'rain': 7.83},
        'September': {'min': 74, 'max': 89, 'rain': 6.02},
        'October': {'min': 68, 'max': 84, 'rain': 3.31},
        'November': {'min': 60, 'max': 78, 'rain': 2.4},
        'December': {'min': 54, 'max': 72, 'rain': 2.64}
    }
    highlight = {'min': 55, 'max': 85, 'rain': 6}
    return render_template('index.html', city='Orlando, FL', months=months,
                           weather=weather, highlight=highlight)


if __name__ == '__main__':
    app.run(debug=True)
