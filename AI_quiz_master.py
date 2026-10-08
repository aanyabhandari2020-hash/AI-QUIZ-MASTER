import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------------------
# AI QUIZ MASTER
# Smart Adaptive Quiz Game
# -----------------------------------------

# Question database
questions = {
    "Easy": [
        {
            "question": "Which language is mainly used for AI and Machine Learning?",
            "options": ["Python", "HTML", "CSS", "SQL"],
            "answer": "Python",
            "hint": "It is famous for libraries like NumPy and TensorFlow."
        },
        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automatic Internet",
                "Advanced Internet",
                "Artificial Information"
            ],
            "answer": "Artificial Intelligence",
            "hint": "It is the technology that allows machines to perform intelligent tasks."
        },
        {
            "question": "Which of these is a programming language?",
            "options": ["Python", "Chrome", "Windows", "Google"],
            "answer": "Python",
            "hint": "It is widely used in AI."
        },
        {
            "question": "Which device is used to type text into a computer?",
            "options": ["Keyboard", "Monitor", "Speaker", "Printer"],
            "answer": "Keyboard",
            "hint": "You press keys on it."
        },
        {
            "question": "What is the brain of a computer commonly called?",
            "options": ["CPU", "Mouse", "Keyboard", "Monitor"],
            "answer": "CPU",
            "hint": "It processes instructions."
        }
    ],

    "Medium": [
        {
            "question": "Which technique allows a computer to learn patterns from data?",
            "options": [
                "Machine Learning",
                "Web Designing",
                "File Management",
                "Typing"
            ],
            "answer": "Machine Learning",
            "hint": "It is a major branch of AI."
        },
        {
            "question": "Which of the following is an example of supervised learning?",
            "options": [
                "Classification using labeled data",
                "Random guessing",
                "Deleting data",
                "Formatting a disk"
            ],
            "answer": "Classification using labeled data",
            "hint": "Supervised learning uses labeled examples."
        },
        {
            "question": "What is the main purpose of a neural network?",
            "options": [
                "Learn patterns from data",
                "Store files only",
                "Print documents",
                "Connect a keyboard"
            ],
            "answer": "Learn patterns from data",
            "hint": "It is inspired by the structure of the human brain."
        },
        {
            "question": "Which Python library is commonly used for data analysis?",
            "options": ["Pandas", "Tkinter", "Random", "Time"],
            "answer": "Pandas",
            "hint": "It works with tables and DataFrames."
        },
        {
            "question": "What does ML stand for?",
            "options": [
                "Machine Learning",
                "Machine Language",
                "Modern Logic",
                "Memory Learning"
            ],
            "answer": "Machine Learning",
            "hint": "It is a subset of AI."
        }
    ],

    "Hard": [
        {
            "question": "Which algorithm is commonly used for classification?",
            "options": [
                "Decision Tree",
                "HTML",
                "CSS",
                "File Explorer"
            ],
            "answer": "Decision Tree",
            "hint": "It makes decisions using branches."
        },
        {
            "question": "What is overfitting in Machine Learning?",
            "options": [
                "Model performs very well on training data but poorly on new data",
                "Model has no data",
                "Computer becomes physically hot",
                "Data is deleted"
            ],
            "answer": "Model performs very well on training data but poorly on new data",
            "hint": "The model has learned the training data too specifically."
        },
        {
            "question": "Which type of learning uses rewards and penalties?",
            "options": [
                "Reinforcement Learning",
                "Supervised Learning",
                "Unsupervised Learning",
                "Transfer Learning"
            ],
            "answer": "Reinforcement Learning",
            "hint": "Think of how an agent learns through trial and error."
        },
        {
            "question": "What is the purpose of a training dataset?",
            "options": [
                "To train the machine learning model",
                "To shut down the computer",
                "To design a webpage",
                "To print results"
            ],
            "answer": "To train the machine learning model",
            "hint": "The model learns patterns from this data."
        },
        {
            "question": "Which concept describes breaking a large dataset into training and testing portions?",
            "options": [
                "Train-Test Split",
                "Data Printing",
                "File Compression",
                "Web Hosting"
            ],
            "answer": "Train-Test Split",
            "hint": "One part teaches the model and the other evaluates it."
        }
    ]
}


# -----------------------------------------
# GAME VARIABLES
# -----------------------------------------

score = 0
lives = 3
question_number = 0

# Starting difficulty
difficulty = "Easy"

# Questions already asked
asked_questions = []

current_question = None


# -----------------------------------------
# AI DIFFICULTY SYSTEM
# -----------------------------------------

def update_difficulty(correct):

    global difficulty

    if correct:
        if difficulty == "Easy":
            difficulty = "Medium"

        elif difficulty == "Medium":
            difficulty = "Hard"

        elif difficulty == "Hard":
            difficulty = "Hard"

    else:
        if difficulty == "Hard":
            difficulty = "Medium"

        elif difficulty == "Medium":
            difficulty = "Easy"

        elif difficulty == "Easy":
            difficulty = "Easy"


# -----------------------------------------
# GET NEXT QUESTION
# -----------------------------------------

def get_question():

    global current_question
    global question_number

    available = []

    for q in questions[difficulty]:
        if q not in asked_questions:
            available.append(q)

    # If all questions at a difficulty are used,
    # allow them again
    if len(available) == 0:
        available = questions[difficulty]

    current_question = random.choice(available)

    asked_questions.append(current_question)

    question_number += 1

    question_label.config(
        text="Question " + str(question_number)
    )

    difficulty_label.config(
        text="AI Difficulty: " + difficulty
    )

    question_text.config(
        text=current_question["question"]
    )

    # Shuffle options
    options = current_question["options"].copy()
    random.shuffle(options)

    for i in range(4):
        buttons[i].config(
            text=options[i],
            state="normal"
        )

    result_label.config(text="")


# -----------------------------------------
# CHECK ANSWER
# -----------------------------------------

def check_answer(selected_answer):

    global score
    global lives

    if selected_answer == current_question["answer"]:

        score += 10

        result_label.config(
            text="Correct! +10 points",
            fg="green"
        )

        update_difficulty(True)

    else:

        lives -= 1

        result_label.config(
            text="Wrong! Correct answer: "
                 + current_question["answer"],
            fg="red"
        )

        update_difficulty(False)

    score_label.config(
        text="Score: " + str(score)
    )

    lives_label.config(
        text="Lives: " + "❤️ " * lives
    )

    # Disable buttons after answering
    for button in buttons:
        button.config(state="disabled")

    if lives <= 0:
        game_over()

    else:
        root.after(1200, get_question)


# -----------------------------------------
# HINT
# -----------------------------------------

def show_hint():

    messagebox.showinfo(
        "AI Hint",
        current_question["hint"]
    )


# -----------------------------------------
# GAME OVER
# -----------------------------------------

def game_over():

    for button in buttons:
        button.config(state="disabled")

    messagebox.showinfo(
        "Game Over",
        "Game Over!\n\n"
        "Your Score: " + str(score) +
        "\nQuestions Attempted: " +
        str(question_number)
    )

    restart_button.config(state="normal")


# -----------------------------------------
# RESTART GAME
# -----------------------------------------

def restart_game():

    global score
    global lives
    global question_number
    global difficulty
    global asked_questions

    score = 0
    lives = 3
    question_number = 0
    difficulty = "Easy"
    asked_questions = []

    score_label.config(
        text="Score: 0"
    )

    lives_label.config(
        text="Lives: ❤️ ❤️ ❤️"
    )

    restart_button.config(
        state="disabled"
    )

    get_question()


# -----------------------------------------
# MAIN WINDOW
# -----------------------------------------

root = tk.Tk()

root.title("AI Quiz Master")
root.geometry("650x600")

root.resizable(False, False)

# -----------------------------------------
# TITLE
# -----------------------------------------

title = tk.Label(
    root,
    text="🧠 AI QUIZ MASTER",
    font=("Arial", 26, "bold")
)

title.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Smart Adaptive Brain Challenge",
    font=("Arial", 13)
)

subtitle.pack()


# -----------------------------------------
# SCORE AREA
# -----------------------------------------

info_frame = tk.Frame(root)

info_frame.pack(pady=20)

score_label = tk.Label(
    info_frame,
    text="Score: 0",
    font=("Arial", 14, "bold")
)

score_label.grid(row=0, column=0, padx=30)

lives_label = tk.Label(
    info_frame,
    text="Lives: ❤️ ❤️ ❤️",
    font=("Arial", 14, "bold")
)

lives_label.grid(row=0, column=1, padx=30)

difficulty_label = tk.Label(
    info_frame,
    text="AI Difficulty: Easy",
    font=("Arial", 14, "bold")
)

difficulty_label.grid(row=0, column=2, padx=30)


# -----------------------------------------
# QUESTION
# -----------------------------------------

question_label = tk.Label(
    root,
    text="Question 1",
    font=("Arial", 14, "bold")
)

question_label.pack(pady=10)


question_text = tk.Label(
    root,
    text="",
    font=("Arial", 17, "bold"),
    wraplength=550,
    justify="center"
)

question_text.pack(pady=20)


# -----------------------------------------
# ANSWER BUTTONS
# -----------------------------------------

buttons = []

for i in range(4):

    button = tk.Button(
        root,
        text="",
        font=("Arial", 12),
        width=45,
        height=2,
        command=lambda i=i:
        check_answer(buttons[i].cget("text"))
    )

    button.pack(pady=5)

    buttons.append(button)


# -----------------------------------------
# HINT BUTTON
# -----------------------------------------

hint_button = tk.Button(
    root,
    text="💡 Get AI Hint",
    font=("Arial", 11, "bold"),
    command=show_hint
)

hint_button.pack(pady=12)


# -----------------------------------------
# RESULT
# -----------------------------------------

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 13, "bold")
)

result_label.pack(pady=5)


# -----------------------------------------
# RESTART BUTTON
# -----------------------------------------

restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 11, "bold"),
    command=restart_game,
    state="disabled"
)

restart_button.pack(pady=10)


# -----------------------------------------
# START GAME
# -----------------------------------------

get_question()

root.mainloop()
