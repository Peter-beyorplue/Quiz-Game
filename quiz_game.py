# quiz_game.py

# Questions and Answers (You can add more)
quiz_questions = [
    {
        "question": "What is the capital of Liberia?",
        "options": ["A) West Point", "B) Brewerville", "C) Tubmanburg", "D) Monrovia"],
        "answer": "D"
    },
    {
        "question": "Who is the present President of Liberia?",
        "options": ["A) Ojuku Vorjolo", "B) Mr. Alexander Cumming", "C) Joseph K. Boakai", "D) George Manneh Weah"],
        "answer": "C"
    },
    {
        "question": "Who many speaker liberia presently have?",
        "options": ["A) 2", "B) 1", "C) None of these", "D) 3"],
        "answer": "1"
    },
    {
        "question": "There is how many counties in Liberia?",
        "options": ["A) 20", "B) 10", "C) 5", "D) 16"],
        "answer": "D"
    }
]

def run_quiz():
    score = 0
    print("Welcome to the Quiz Game!\n")

    for i, question in enumerate(quiz_questions):
        print(f"Question {i+1}: {question['question']}")
        for option in question['options']:
            print(option)

        user_answer = input("Your answer (A, B, C, D): ").strip().upper()

        if user_answer == question["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {question['answer']}.\n")

    print(f"Quiz Over! You scored {score} out of {len(quiz_questions)}.")

if __name__ == "__main__":
    run_quiz()
