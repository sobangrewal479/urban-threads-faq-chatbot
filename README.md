# Urban Threads Co. FAQ Chatbot

A client-style FAQ chatbot for a mock online clothing store, built with Python and Streamlit.

This project was created as a beginner-friendly freelance portfolio project. It helps a small clothing store answer repeated customer questions about shipping, returns, exchanges, payments, sizing, orders, discounts, and contact details.

---

## Project Goal

Urban Threads Co. receives repeated customer questions about store policies. The goal of this chatbot is to give customers quick answers from a fixed FAQ knowledge base and reduce repetitive support work.

---

## Features

- Customer-facing FAQ chatbot
- Answers from a fixed JSON FAQ knowledge base
- Fallback response for unsupported questions
- Question logging to CSV
- Simple Streamlit web app
- Automated tests with pytest
- Beginner-friendly local setup

---

## Tech Stack

- Python
- Streamlit
- JSON
- CSV logging
- pytest
- Git and GitHub

---

## Folder Structure

```text
urban_threads_faq_chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── faqs.json
│
├── logs/
│   └── questions_log.csv
│
├── src/
│   ├── faq_engine.py
│   └── logger.py
│
└── tests/
    ├── conftest.py
    ├── test_faq_engine.py
    └── test_logger.py