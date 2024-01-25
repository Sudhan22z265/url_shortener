from flask import Flask,render_template,request,redirect,url_for,flash
import json,os
app = Flask(__name__)
app.secret_key = 'abcdef'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/your-url',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        urls={}
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
        if request.form['code'] in urls.keys():
            flash('The short name has already been taken! Try another..')
            return redirect(url_for('index'))
        urls[request.form['code']] = {"url": request.form['url']}
        with open('urls.json','w') as url_file:
            json.dump(urls,url_file)
        return render_template('your_url.html',code=request.form['code'])
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)