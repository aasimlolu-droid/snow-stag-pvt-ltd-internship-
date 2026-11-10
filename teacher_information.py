
# Program to store teacher information using dictionaries

teachers = [
    {
        "Teacher ID": 101,
        "Teacher Name": "Mr. Ahmad",
        "Subject": "Python",
        "Email Address": "ahmad@gmail.com"
    },
    {
        "Teacher ID": 102,
        "Teacher Name": "Mr. Tariq",
        "Subject": "Artificial Intelligence",
        "Email Address": "tariq@gmail.com"
    },
    {
        "Teacher ID": 103,
        "Teacher Name": "Ms. Ayesha",
        "Subject": "Mathematics",
        "Email Address": "ayesha@gmail.com"
    },
    {
        "Teacher ID": 104,
        "Teacher Name": "Mr. Imran",
        "Subject": "Computer Science",
        "Email Address": "imran@gmail.com"
    },
    {
        "Teacher ID": 105,
        "Teacher Name": "Ms. Sana",
        "Subject": "English",
        "Email Address": "sana@gmail.com"
    }
]

# Display all teacher information

print("Teacher Information")
print("-------------------")

for teacher in teachers:
    print("Teacher ID:", teacher["Teacher ID"])
    print("Teacher Name:", teacher["Teacher Name"])
    print("Subject:", teacher["Subject"])
    print("Email Address:", teacher["Email Address"])
    print("-------------------")
