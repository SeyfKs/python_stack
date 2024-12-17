from flask import Flask, render_template, request, redirect, session  # Import session

app = Flask(__name__)
app.secret_key = "secret_key"  # Required for using sessions


@app.route('/')
def index():
    # Render the form for input
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Store form data in the session
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect("/show")  # Redirect to the show page


@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    # Retrieve user info from session
    name = session.get('name', 'Unknown')
    email = session.get('email', 'Unknown')
    return render_template("show.html", name=name, email=email)


if __name__ == "__main__":
    app.run(debug=True)

