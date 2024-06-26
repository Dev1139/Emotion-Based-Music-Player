from flask import Flask, render_template, redirect, url_for
from camera import detect_emotion  # Import the function from your Python file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/emotion_detection", methods = ['POST'])
def emotion_detection():
    result = detect_emotion()  # Execute the function
    if result == "Happy":
        return redirect(url_for('happy_music'))
    elif result == "Sad":
        return redirect(url_for('sad_music'))
    elif result == "Neutral":
        return redirect(url_for('neutral_music'))
    elif result == "Fearful":
        return redirect(url_for('fear_music'))
    elif result == "Angry":
        return redirect(url_for('angry_music'))
    elif result == "Disgusted":
        return redirect(url_for('disgust_music'))
    elif result == "Surprised":
        return redirect(url_for('surprise_music'))
    else:
        return redirect(url_for('exception'))
    

@app.route("/happy_music")
def happy_music():
    return render_template('Happy.html')

@app.route("/sad_music")
def sad_music():
    return render_template('Sad.html')

@app.route("/neutral_music")
def neutral_music():
    return render_template('Neutral.html')

@app.route("/fear_music")
def fear_music():
    return render_template('Fear.html')

@app.route("/angry_music")
def angry_music():
    return render_template('Angry.html')

@app.route("/disgust_music")
def disgust_music():
    return render_template('Disgust.html')

@app.route("/surprise_music")
def surprise_music():
    return render_template('surprise.html')

@app.route("/exception")
def exception():
    return render_template('Exception.html')

if __name__ == '__main__':
    app.run(debug=True)