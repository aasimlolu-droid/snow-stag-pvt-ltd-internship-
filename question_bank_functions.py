
# Question Bank Program using Functions

teachers = []
questions = []


# Adding a teacher
def add_teacher():
    tid = input("Enter teacher ID: ")
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")
    email = input("Enter email: ")

    teacher = {
        "ID": tid,
        "Name": name,
        "Subject": subject,
        "Email": email
    }

    teachers.append(teacher)
    print("Teacher added successfully.")


# Adding a question
def add_question():
    qid = input("Enter question ID: ")
    subject = input("Enter subject: ")
    question = input("Enter question: ")

    q = {
        "ID": qid,
        "Subject": subject,
        "Question": question
    }

    questions.append(q)
    print("Question added successfully.")


# Displaying all questions
def display_questions():
    if len(questions) == 0:
        print("No questions available.")
    else:
        for q in questions:
            print("\nQuestion ID:", q["ID"])
            print("Subject:", q["Subject"])
            print("Question:", q["Question"])


# Searching questions by subject
def search_questions():
    sub = input("Enter subject name: ")
    found = False

    for q in questions:
        if q["Subject"].lower() == sub.lower():
            print(q["Question"])
            found = True

    if found == False:
        print("No questions found.")


# Counting questions for each subject
def count_questions():
    count = {}

    for q in questions:
        sub = q["Subject"]

        if sub in count:
            count[sub] = count[sub] + 1
        else:
            count[sub] = 1

    for sub in count:
        print(sub, ":", count[sub])


# Main menu
while True:
    print("\n--- Question Bank ---")
    print("1. Add Teacher")
    print("2. Add Question")
    print("3. Display Questions")
    print("4. Search Questions")
    print("5. Count Questions")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_teacher()

    elif choice == "2":
        add_question()

    elif choice == "3":
        display_questions()

    elif choice == "4":
        search_questions()

    elif choice == "5":
        count_questions()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Wrong choice. Try again.")
