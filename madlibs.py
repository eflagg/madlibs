from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    """User wants to play or not"""

    response = request.args.get("yesno")

    if response == "no":
        return render_template("goodbye.html")

    elif response == "yes":
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Inputs user info into madlib story"""

    person = request.args.get("person")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    color = request.args.get("color")
    verb = request.args.get("verb")
    animals = request.args.getlist("animal")
    list_of_madlibs = ["madlib.html", "madlibs2.html"]
    html = choice(list_of_madlibs)


    return render_template(html, person=person, noun=noun, 
                            adjective=adjective, color=color, verb=verb, animals=animals)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
