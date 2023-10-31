class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Define quiz questions
questions = [
    Question("What is the capital of France?\n(a) Paris\n(b) London\n(c) Berlin\n", "a"),
    Question("Which planet is known as the Red Planet?\n(a) Mars\n(b) Jupiter\n(c) Venus\n", "a"),
    Question("What is the largest mammal in the world?\n(a) Elephant\n(b) Blue Whale\n(c) Giraffe\n", "b")
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt).lower()
        if answer == question.answer:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is: " + question.answer + "\n")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct.")

# Run the quiz
if __name__ == "__main__":
    run_quiz(questions)
