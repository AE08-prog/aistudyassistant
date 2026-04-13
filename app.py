from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_questions(notes, difficulty):
    notes = notes.lower()

    # Pick topic
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

    # Difficulty templates
    if difficulty == "easy":
        templates = [
            "What is {topic}?",
            "Define {topic}.",
            "What does {topic} do?"
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
            "Compare and evaluate {topic} with another biological process.",
            "Explain in detail the mechanisms behind {topic}."
        ]

    # Generate multiple questions
    questions = []
    for _ in range(3):  # 3 questions per session
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
    app.run()