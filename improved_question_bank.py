
# Improved Question Bank Program

teachers = []
questions = []


# Function to add a teacher
def add_teacher():
    tid = input("Enter Teacher ID: ")
    name = input("Enter Teacher Name: ")
    subject = input("Enter Subject: ")
    email = input("Enter Email: ")

    teacher = {
        "ID": tid,
        "Name": name,
        "Subject": subject,
        "Email": email
    }

    teachers.append(teacher)
    print("Teacher added successfully!")


# Function to display teachers
def display_teachers():
    if len(teachers) == 0:
        print("No teachers added yet.")
    else:
        for t in teachers:
            print("\nTeacher ID:", t["ID"])
            print("Name:", t["Name"])
            print("Subject:", t["Subject"])
            print("Email:", t["Email"])


# Function to add questions
def add_question():
    qid = input("Enter Question ID: ")

    # Checking whether question ID already exists
    for q in questions:
        if q["ID"] == qid:
            print("This Question ID already exists.")
            return

    tid = input("Enter Teacher ID: ")

    # Checking whether teacher exists
    teacher_found = False

    for t in teachers:
        if t["ID"] == tid:
            teacher_found = True
            break

    if teacher_found == False:
        print("Teacher not found. Add the teacher first.")
        return

    subject = input("Enter Subject: ")
    question = input("Enter Question: ")
    marks = int(input("Enter Marks: "))

    new_question = {
        "ID": qid,
        "Teacher ID": tid,
        "Subject": subject,
        "Question": question,
        "Marks": marks
    }

    questions.append(new_question)
    print("Question added successfully!")


# Function to display all questions
def display_questions():
    if len(questions) == 0:
        print("No questions available.")
    else:
        for q in questions:
            print("\nQuestion ID:", q["ID"])
            print("Teacher ID:", q["Teacher ID"])
            print("Subject:", q["Subject"])
            print("Question:", q["Question"])
            print("Marks:", q["Marks"])


# Main menu
while True:
    print("\n===== Question Bank =====")
    print("1. Add Teacher")
    print("2. Display Teachers")
    print("3. Add Question")
    print("4. Display Questions")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_teacher()

    elif choice == "2":
        display_teachers()

    elif choice == "3":
        add_question()

    elif choice == "4":
        display_questions()

    elif choice == "5":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Try again.")
