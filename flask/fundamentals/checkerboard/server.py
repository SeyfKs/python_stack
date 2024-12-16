from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def play():
    return render_template('index.html', num=4,num1=4, color="blue",color2="red")

@app.route('/<int:num1>')
def play_num1(num1):
    return render_template('index.html',num=8, num1=num1, color="blue", color2="red")

@app.route('/<int:num1>/<int:num>')
def play_num(num1,num):
    return render_template('index.html',num=num, num1=num1, color="blue",color2="red")

@app.route('/<int:num1>/<int:num>/<color>/<color2>')
def play_num2(num1,num,color,color2):
    return render_template('index.html',num=num, num1=num1, color=color,color2=color2)

if __name__=="__main__":
    app.run(debug=True)