#from flask import Flask
#app = Flask(__name__)

#@app.route('/')
#def hello_world():
    #return '<h1>Hello, World!</h1>'

from flask import Flask, render_template

app = Flask(name)

@app.route('/hello-world')
def view_hello_world():
    return render_template('hello_world.html')