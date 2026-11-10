
# Question Paper Generator

import random

questions = []


# Function to add questions
def add_question():
    qid = input("Enter Question ID: ")

    for q in questions:
        if q["ID"] == qid:
            print("Question ID already exists.")
            return

    subject = input("Enter subject: ")
    question = input("Enter question: ")
    marks = int(input("Enter marks: "))

    q = {
        "ID": qid,
        "Subject": subject,
        "Question": question,
        "Marks": marks
    }

    questions.append(q)
    print("Question added successfully.")


# Function to display questions
def display_questions():
    if len(questions) == 0:
        print("No questions available.")
    else:
        for q in questions:
            print("\nID:", q["ID"])
            print("Subject:", q["Subject"])
            print("Question:", q["Question"])
            print("Marks:", q["Marks"])


# Function to generate question paper
def generate_paper():
    subject = input("Enter subject: ")
    number = int(input("Enter number of questions: "))

    available = []

    for q in questions:
        if q["Subject"].lower() == subject.lower():
            available.append(q)

    if len(available) < number:
        print("Not enough questions available.")
        print("Available questions:", len(available))
        return

    # Select questions randomly
    selected = random.sample(available, number)

    print("\n----- Question Paper -----")
    print("Subject:", subject)
    print("Total Questions:", number)

    total = 0

    for i, q in enumerate(selected, 1):
        print("\n", i, ".", q["Question"])
        print("Marks:", q["Marks"])
        total = total + q["Marks"]

    print("\nTotal Marks:", total)
    print("--------------------------")


# Main menu
while True:
    print("\n1. Add Question")
    print("2. Display Questions")
    print("3. Generate Question Paper")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_question()

    elif choice == "2":
        display_questions()

    elif choice == "3":
        generate_paper()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Wrong choice. Try again.")
