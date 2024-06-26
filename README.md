#Overview
The Emotion-Based Music Player is a project that utilizes facial emotion detection to play music that matches the user's current mood. The application captures an image from the webcam, detects the user's emotion using a pre-trained neural network, and then plays a curated playlist corresponding to the detected emotion.

#Project Structure
camera.py: Handles the emotion detection using a webcam and a pre-trained neural network.
app.py: The Flask web application that provides the user interface and routes for the emotion-based music player.
index.html: The main page of the web application.
Exception.html: Page displayed when no emotion is detected.
Happy.html, Sad.html, Fear.html, Angry.html, Surprise.html, Disgust.html, Neutral.html: Pages that play music corresponding to the detected emotion.
styles.css: Styles for the main page.
player_style.css: Styles for the music player pages.

#Dependencies
numpy
opencv-python (cv2)
tensorflow
flask

#Setup Instructions
1. Clone the repository:
git clone https://github.com/your-username/emotion-based-music-player.git
cd emotion-based-music-player

2. Install the dependencies:
pip install numpy opencv-python tensorflow flask

3.Download the pre-trained model:
Ensure you have the file model.h5 in the project directory.

4.Run the application:
python app.py

5.Access the application:
Open your web browser and go to http://127.0.0.1:5000.
