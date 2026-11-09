
# Creating a question bank
questions = {
    "Python": [
        "What is Python?",
        "What are variables?",
        "What is a loop?",
        "What is a function?",
        "What is a list?"
    ],
    "AI": [
        "What is Artificial Intelligence?",
        "What is Machine Learning?",
        "What is an expert system?",
        "What are neural networks?",
        "What is NLP?"
    ]
}

# Displaying subjects
print("Available Subjects:")
print("Python")
print("AI")

# Taking input
subject = input("Enter subject name: ").strip().title()

if subject == "Ai":
    subject = "AI"

if subject in questions:

    number = int(input("Enter number of questions required: "))

    if number > 0 and number <= len(questions[subject]):

        print("\nGenerating a Question Paper QUESTION PAPER")
        print("Subject:", subject)
        print("Total Questions:", number)
        print("--------------------------")

        for i in range(number):
            print(str(i + 1) + ".", questions[subject][i])

    else:
        print("Please enter a valid number of questions.")

else:
    print("Subject not found.")
