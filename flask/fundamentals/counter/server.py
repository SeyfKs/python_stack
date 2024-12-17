from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'count' not in session:
        session['count'] = 0

    if request.method == 'POST':
        session['count'] += 1

    return render_template('index.html', count=session['count'])


@app.route('/reset')
def reset():
    session.pop('count')
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
