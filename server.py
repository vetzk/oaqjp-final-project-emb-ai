"""Flask web server for running emotion detection on user-provided text."""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    """Analyze text from the request and return formatted emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")
    result = emotion_detector(text_to_analyze)
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"
    return (f"For the given statement, the system response is "
    f"{result}. The dominant emotion is <b>{result['dominant_emotion']}</b>")

@app.route("/")
def render_index_page():
    """Render the main index HTML page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
