# AI Exam Generator (Flask Web App)
https://aistudyassistant-hur6.onrender.com/
## Overview

This is a web-based exam generator built using Python and Flask. It converts study notes into structured exam-style questions with different difficulty levels (easy, medium, hard).

The project is designed to support active recall learning by turning passive study notes into interactive questions.

---

## Features

* Input study notes through a web interface
* Generates multiple exam-style questions per session
* Three difficulty levels:

  * Easy (definitions and basic understanding)
  * Medium (explanations and processes)
  * Hard (analysis and evaluation)
* Generates 3 unique questions per session
* Simple and clean web interface
* Supports static assets (images like logos or backgrounds)

---

## Built With

* Flask
* Python 3
* HTML (Jinja templates)
* Randomized logic system

---

## Project Structure

```text id="project_structure_final"
aistudyassistant/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── brainbolt.png
├── requirements.txt
└── README.md
```

---

## Static Files

The `static/` folder is used to store non-changing assets such as:

* Images (logos, icons, backgrounds)
* Future CSS files
* Future JavaScript files

Example usage in HTML:

```html id="static_usage_final"
<img src="{{ url_for('static', filename='brainbolt.png') }}">
```

---

## How to Run Locally

### 1. Install dependencies

```bash id="run1"
pip install flask
```

### 2. Run the application

```bash id="run2"
python app.py
```

### 3. Open in browser

```text id="run3"
http://127.0.0.1:5000
```

---

## Deployment

This project is deployed using:

* Render
* GitHub integration for automatic updates

### Build Command

```bash id="build"
pip install -r requirements.txt
```

### Start Command

```bash id="start"
python app.py
```

---

## How It Works

1. User enters study notes
2. System detects key topic
3. Generates multiple exam-style questions
4. Adjusts difficulty based on selected level
5. Displays results in a clean UI

---

## Future Improvements

* Add AI-powered question generation
* Add answer checking system
* Add scoring and progress tracking
* Add user login system
* Improve UI with animations and modern design

---

## Author

Created by Khalifa
Developed as a university portfolio project demonstrating web development and interactive learning system design.

---

