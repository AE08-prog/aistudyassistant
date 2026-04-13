# AI Exam Generator (Flask App)

## Overview

This is a web-based exam generator built using Python and Flask. It converts study notes into structured exam-style questions with different difficulty levels (easy, medium, hard).

The purpose of this project is to simulate an intelligent learning system that supports active recall and self-testing for students.

---

## Features

* Input study notes through a web interface
* Generates multiple exam-style questions per session
* Three difficulty levels:

  * Easy (definitions and basic understanding)
  * Medium (explanations and processes)
  * Hard (analysis and evaluation)
* Generates 3 questions per session
* Simple and clean web interface
* Fully works without external AI APIs

---

## Built With

* Flask (Python web framework)
* Python 3
* HTML (Jinja templates)
* Randomized logic system

---

## Project Structure

```
aistudyassistant/
│
├── app.py
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

---

## How to Run Locally

### 1. Install dependencies

```
pip install flask
```

### 2. Run the application

```
python app.py
```

### 3. Open in browser

```
http://127.0.0.1:5000
```

---

## Deployment

This project can be deployed using platforms such as:

* Render
* GitHub + cloud hosting services

### Build Command

```
pip install -r requirements.txt
```

### Start Command

```
python app.py
```

---

## How It Works

1. User enters study notes
2. System detects key topics
3. Generates multiple exam-style questions
4. Adjusts difficulty based on selected level

---

## Future Improvements

* Integration with AI-based question generation
* Automatic answer checking system
* Score tracking and grading system
* User accounts and login system
* Progress tracking dashboard

---

## Author

Created by Khalifa
Project developed for educational and university portfolio purposes
