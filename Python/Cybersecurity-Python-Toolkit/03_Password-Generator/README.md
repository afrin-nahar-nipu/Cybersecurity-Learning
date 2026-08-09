# 🔐 Password Generator

A professional command-line Password Generator built with Python.

This project generates random passwords based on user-defined length and
special-character preferences. It also evaluates password strength and
allows generated passwords to be saved locally with a timestamp.

---

## 📌 Project Overview

The Password Generator is a Python-based cybersecurity utility designed to
generate random and customizable passwords.

This project demonstrates practical Python programming concepts such as:

- Functions
- Modular Programming
- Random Password Generation
- Input Validation
- Password Strength Analysis
- File Handling
- Date and Time Handling
- Directory Management
- Exception Handling

---

## ✨ Features

- 🔐 Generate random passwords
- 📏 Custom password length
- 🔢 Generate multiple passwords at once
- 🔣 Optional special characters
- 💪 Password strength checking
- 💾 Save generated passwords locally
- 🕒 Save generation date and time
- 📂 Automatic output directory creation
- 🛡️ Input validation
- ⚠️ Exception handling
- 🖥️ Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- `random`
- `string`
- `os`
- `datetime`

No external Python packages are required.

---

## 📂 Project Structure

```text
03_Password-Generator/
│
├── generated_passwords/
│   └── passwords.txt
│
├── main.py
├── password_generator.py
├── utils.py
├── README.md
└── .gitignore

💪 Password Strength Checking

The program evaluates generated passwords based on:

Password length
Lowercase characters
Uppercase characters
Numbers
Special characters

The strength result is categorized as:

🔴 Weak
🟡 Medium
🟢 Strong

💾 Password Storage

Generated passwords are saved locally in:

generated_passwords/passwords.txt

The saved information includes:

Generated password
Password strength
Generation date and time

The generated_passwords directory is automatically created by the program
if it does not already exist.

🔒 Security Note

This project is developed for educational and cybersecurity learning
purposes.

Generated passwords should not be committed to a public GitHub repository.

The generated password history file is excluded from Git tracking using
.gitignore.

For real-world password management, use a trusted password manager instead
of storing passwords in plain text.

For security-sensitive password generation, Python's secrets module is
recommended over the standard random module.

📚 Learning Objectives

This project was developed to practice:

Python fundamentals
Functions
Modular programming
Randomized data generation
String manipulation
File handling
Exception handling
Directory management
Date and time handling
Basic cybersecurity-oriented programming
Git and GitHub project management

🔮 Future Improvements
 Use Python secrets for security-focused password generation
 Guarantee at least one uppercase character
 Guarantee at least one lowercase character
 Guarantee at least one number
 Guarantee at least one special character
 Add user-selectable character categories
 Add password entropy estimation
 Improve password strength scoring
 Add CSV export
 Develop a GUI version
 Add secure password history management
👩‍💻 Author

Afrin Nahar Nipu

Cybersecurity Python Toolkit — Project 03