from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    question = ""
    feedback = ""

    if request.method == "POST":
        notes = request.form.get("notes")

        if notes:
            question = "Sample Question: What is photosynthesis?"
            feedback = "Your answer will be checked in future AI version."

    return render_template("index.html", question=question, feedback=feedback)

if __name__ == "__main__":
    app.run()