from flask import Flask
import random
app = Flask(__name__)
#PASS YOUR GUESS IN THE URL BAR AS AN ARGUMAENT
@app.route("/")
def home():
    return '<h1 style="size:12;">Guess the number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'
@app.route('/<int:Guess>')
def guess(Guess):

    selected_number=random.choice(list(range(10)))


    if Guess==selected_number:
        return '<h1 styl="color:green;">You guessed it right</h1>'\
               '<img src=" https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif Guess < selected_number:
        return '<h1 style="color:red;">It is too low</h1>'\
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="color:red;">It is too High</h1>'\
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'









if __name__=='__Higher_lower Game(Flask)__':
    app.run(debug=True,use_reloader=True)
