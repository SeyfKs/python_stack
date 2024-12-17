from flask import Flask, render_template, request, redirect, session, url_for
import random

app = Flask(__name__)
app.secret_key = "secret_key_for_session"  


@app.route("/", methods=["GET", "POST"])
def index():
    if "number" not in session:
        session["number"] = random.randint(1, 100)
    message = ""
    color = ""
    if request.method == "POST":
        try:
            guess = int(request.form["guess"])
            if guess < session["number"]:
                message = "Too Low!"
                color = "blue"
            elif guess > session["number"]:
                message = "Too High!"
                color = "red"
            else:
                message = "Correct! You guessed the number!"
                color = "green"
        except ValueError:
            message = "Please enter a valid number between 1 and 100."
            color = "black"
    return render_template("index.html", message=message, color=color)


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
