from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/your-url',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        return render_template('your_url.html',code=request.form['code'])
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)