from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/your-url')
def about():
    return render_template('your_url.html',code=request.args['code'])


if __name__ == '__main__':
    app.run(debug=True)