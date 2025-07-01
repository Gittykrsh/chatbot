# 🧠 Project 8: TamizhanBot - A Rule-Based Chatbot

Tamizhan Bot is a simple yet intelligent **rule-based chatbot** designed to interact with users and answer queries about **Tamizhan Skills** — such as courses, instructors, fees, internships, and more.

---

## 🚀 Features

| Feature                        | Description                                                                 |
|-------------------------------|-----------------------------------------------------------------------------|
| 🤖 Rule-Based Chatbot         | Uses regex and keyword matching to identify user intent.                    |
| 🗣️ Dynamic Greetings           | Recognizes full names and responds personally.                              |
| 📚 Course Info Support        | Provides details about offered courses and learning modes.                 |
| 👨‍🏫 Instructor Info           | Shares information about instructors and their experience.                 |
| 💼 Internship & Placement     | Answers queries about internships and placement support.                    |
| 💸 Fee Details                | Informs about course pricing and affordability.                             |
| ⏱️ Duration Info              | Provides course duration in weeks/months.                                   |
| 🧠 Help & Suggestions         | Offers suggestions when user is confused.                                  |
| 📝 Fuzzy Matching             | Accepts slight spelling mistakes in user input.                             |
| 👋 Exit Commands              | Understands exit phrases like 'bye', 'exit', etc.                           |
| 🤖 Typing Simulation          | Bot simulates typing effect for better UX.                                 |

---

## 💡 Example Interactions

```txt
👋 What's your name?
Hello, I am Shakyasimha Das
🧠 Great to meet you, Shakyasimha Das!
💬 I'm TamizhanBot! Would you like to know about Tamizhan Skills? (yes/no)
yes
📚 Awesome! Here's what we offer :
→ We offer Python, Web Development, AI/ML, and Internship-based learning programs.

👩‍💻 You can type your question below. (Type 'exit' to quit)

How long are the courses?
→ Most courses are 4 to 8 weeks long, with flexible timing. 📅

Tell me about your instructors
→ Every instructor at Tamizhan Skills ensures you get placement-level skills. 💪
```

---

## ⚙️ Technologies Used

- Python 🐍
- `re` module for pattern matching
- `difflib` for fuzzy matching
- `time` and `random` for delay and variation
- Clean terminal-based UI

---

## 📦 How to Run

```bash
python test.py
```

---

## 🙋‍♂️ Additional Notes

- You can type natural language questions like:
  - *"How much are the fees?"*
  - *"Who are your instructors?"*
  - *"Do you offer internships?"*

- Bot also supports casual talk like:
  - *"Hello"*, *"Thanks"*, *"bye"*

---

Made with ❤️ as part of the **Tamizhan Skills Internship Projects**.
