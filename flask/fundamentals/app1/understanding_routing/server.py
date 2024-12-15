from flask import Flask  

app = Flask(__name__)    

@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          
def dojo():
    return 'Dojo!'

@app.route('/say/<name>') 
def say(name):
    return f"Hi, {name}!"


@app.route('/repeat/<int:num>/<string:name>') 
def repeat(name, num):
    return f"{name * num}"


if __name__=="__main__": 
    app.run(debug=True)    

