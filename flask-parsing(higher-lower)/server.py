import random
from flask import Flask
app = Flask(__name__)

number = random.randint(0, 9)
print(number)

@app.route("/")
def home():
    return (f"<h1>Guess a number between 0 and 9</h1>"
            f"<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNzd4ZTFsc3k3b21sYTVzNG56NXA4NHZ6ZXozam84ajljdDZ3eW5qaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/hvLwZ5wmarjnNKEJqq/giphy.gif'>")

@app.route("/<int:guess>")
def guess_number(guess):
    if guess < number:
        return ("<h1 style='color: red'>Too low, try again.</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm53cjJ6ZXY0anRrc3J3bHZnM3BobG1qOGJxMHNnaW5mOHJuOW4waSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKHWfu68Q6XOz2I6Y/giphy.gif'>")
    elif guess > number:
        return ("<h1 style='color: purple'>Too high, try again.</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnd5bTd3bmgyaHFjdnhheXMwdnp0aGFlM21xZDYwbGFvNGRvdDRuZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3og0IuWMpDm2PdTL8s/giphy.gif'>")
    elif guess == number:
        return ("<h1 style='color: green'>YOU FIND ME!</h1>"
                "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWoxbWxpbnoyc29zMXJuODRtNmltYzR0dmdrYnppcGM5b2lycDF3ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/10UB1BfC4EKll6/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)
