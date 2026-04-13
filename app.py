from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generate_questions(notes, difficulty):
    notes = notes.lower()

    # detect topic
    if "photosynthesis" in notes:
        topic = "photosynthesis"
    elif "force" in notes:
        topic = "force"
    elif "cell" in notes:
        topic = "the cell"
    elif "respiration" in notes:
        topic = "cellular respiration"
    else:
        topic = "the main concept"

    # difficulty-based templates
    if difficulty == "easy":
        templates = [
            "What is {topic}?",
            "Define {topic}.",
            "State one fact about {topic}."
        ]
    elif difficulty == "medium":
        templates = [
            "Explain how {topic} works.",
            "Why is {topic} important?",
            "Describe the process of {topic}."
        ]
    else:  # hard
        templates = [
            "Analyse the importance of {topic} in living systems.",
            "Evaluate the role of {topic} in science.",
            "Explain in detail how {topic functions and why it matters."
        ]

    questions = []
    for _ in range(3):
        q = random.choice(templates).format(topic=topic)
        questions.append(q)

    return questions


@app.route("/", methods=["GET", "POST"])
def home():
    questions = []

    if request.method == "POST":
        notes = request.form.get("notes")
        difficulty = request.form.get("difficulty", "easy")

        if notes:
            questions = generate_questions(notes, difficulty)

    return render_template("index.html", questions=questions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))