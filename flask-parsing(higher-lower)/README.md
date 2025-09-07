# Number Guessing Game - Flask Web App 🎲

This is a simple **Number Guessing Game** built with Python and Flask.  
The user tries to guess a randomly generated number between 0 and 9.  
The app responds with a message and a fun GIF depending on whether the guess is too low, too high, or correct.  

---

## Features ✨

- Random number generation (0-9)  
- Response based on the guess:
  - **Too low**: The guess is lower than the number  
  - **Too high**: The guess is higher than the number  
  - **YOU FIND ME!**: Correct guess  
- Fun GIFs accompany each response  
- Simple web interface with Flask  

---

## Installation 🛠

1. Make sure Python is installed (Python 3.8+ recommended)  
2. Install required packages:
```
pip install flask
```

Open your browser and go to http://127.0.0.1:5000/

---

## How to Play 🎮
On the home page, you will see the message "Guess a number between 0 and 9".

Make a guess by adding it to the URL:

```
http://127.0.0.1:5000/5
```

Depending on your guess, you will see:

- Too low (red) if your guess is smaller than the number

- Too high (purple) if your guess is bigger than the number

- YOU FIND ME! (green) if your guess is correct
