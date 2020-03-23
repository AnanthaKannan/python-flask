from flask import Flask
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login',methods = ['POST'])
def login():
    print(request.form)
    # user = request.form['nm']
    return 'hello'


if __name__ == '__main__':
    app.run(debug = True)