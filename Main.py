from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route('/test-of-paths')
def index2():
    return "Test Succeeded"


if __name__ == '__main__':
    app.run(debug=True)
