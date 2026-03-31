# 🧠 Interview Feature Extraction (Mini Flexor)

Turn unstructured interview text into structured, queryable data using an LLM.

## 📌 Overview

This project demonstrates how to extract meaningful insights from raw interview transcripts using OpenAI’s API.
It converts free text into structured JSON features that can later be stored, analyzed, or queried.

---

## ⚡ Example

### Input

```text
"The kitchen feels crowded and I need more storage."
```

### Output

```json
{
  "mentions_kitchen": true,
  "wants_storage": true,
  "mentions_light": false,
  "sentiment": "negative",
  "summary": "The kitchen is crowded and needs more storage."
}
```

---

## 🏗️ How It Works

1. A transcript is passed to the `extract_features` function
2. A prompt is sent to an LLM (OpenAI API)
3. The model extracts structured fields
4. The response is parsed into valid JSON

Core logic is implemented in:

* `extract_features(transcript)` 

---

## 📦 Features Extracted

| Feature          | Description                    |
| ---------------- | ------------------------------ |
| mentions_kitchen | Whether kitchen is mentioned   |
| wants_storage    | Whether storage is needed      |
| mentions_light   | Whether lighting is mentioned  |
| sentiment        | positive / negative / neutral  |
| summary          | Short summary of the interview |

---

## ⚙️ Installation

```bash
pip install openai python-dotenv
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

```python
from main import extract_features

result = extract_features("I love the natural light in the living room.")
print(result)
```

---

## 🧠 Use Cases

* User interview analysis
* Product research insights
* Customer feedback processing
* Survey automation

---

## 🚀 Future Improvements

* Store results in a SQL database
* Batch processing for multiple interviews
* Add more feature categories
* Build a simple UI (Streamlit)
* Connect to dashboards / analytics tools

---

## 💡 Why This Project

This project mimics real-world systems that:

* Convert unstructured text → structured data
* Enable querying insights at scale
* Power data-driven decision making

---

## 🛠️ Tech Stack

* Python
* OpenAI API
* dotenv
