Got you — here’s a **single, clean, copy-pasteable README.md** you can drop straight into your repo. It’s written to match the task rubric and score well with reviewers:

```md
# Message Similarity Finder (TF-IDF + Cosine Similarity)

## 📌 Overview
This project is a terminal-based Python application that finds the most similar messages from a predefined message database using **TF-IDF vectorization** and **cosine similarity**.

The application embeds all messages locally (no external APIs) and returns the **Top 3 most similar messages** for a given user query along with similarity scores.

---

## 🧠 Approach

- A small message database is hardcoded across multiple categories:
  - Greetings  
  - Tech Support  
  - Product Inquiries  
  - Complaints  

- **TF-IDF (Term Frequency–Inverse Document Frequency)** is used to convert text messages into numerical vectors.

- **Cosine Similarity** is used to measure semantic similarity between the user input and stored messages.

- The system returns the **Top 3 most similar messages** with similarity scores.

All processing is done locally. No external APIs or vector databases are used.

---

## 🏗️ Project Structure

```

message-similarity/
├── main.py
├── embeddings/
│   └── embedding_service.py
├── utils/
│   └── similarity.py
├── data/
│   └── messages.py
├── requirements.txt
├── README.md
└── .gitignore

````

---

## ⚙️ Setup Instructions

### 1. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How To Run

### Option 1: Command-line argument

```bash
python main.py "I need help with my account"
```
or
```bash
python main.py "I need help with my account" --topk 5
```
This will return the Top 5 most similar messages.
If --topk is not provided, the application defaults to Top 3 results. 
### Option 2: Interactive mode

```bash
python main.py
Enter your message: I need help with my account
```

---

## 📤 Sample Output

```
Top 3 Similar Messages:

1. [Score: 88.23%] "How do I reset my password?"
2. [Score: 74.91%] "I cannot log into my account"
3. [Score: 69.12%] "My app is not working"

⏱ Execution Time: 0.0021 seconds
```

---

## 🧪 Test Cases

| Input                         | Expected Result                  |
| ----------------------------- | -------------------------------- |
| How can I change my password? | Tech support messages            |
| Good afternoon                | Greeting messages                |
| The weather is nice today     | Low similarity (unrelated input) |
| cancel my subscription        | Complaint-related messages       |
| hello                         | Greeting messages                |

---

## ⭐ Bonus Features Implemented

- User can specify number of results using `--topk` flag  
- Similarity score displayed as percentage  
- Color-coded output (green = high, yellow = medium, red = low similarity)  
- Execution time displayed for each query  
- Supports both CLI and interactive input modes 

---

## 📦 Dependencies

* numpy
* scikit-learn
* colorama

All dependencies run locally. No external APIs are used.

---

## 📎 Notes

* The embedding method is modular and can be replaced with transformer-based embeddings in the future.
* The project is designed for small in-memory datasets as required by the task.
* The number of returned results can be configured using the `--topk` flag.

