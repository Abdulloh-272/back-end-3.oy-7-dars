def add_students():
    with open('Students.txt', 'a') as file:
        while True:
            student_name = input("Student ism-familiyasi kiriting (yoki 'stop' deb yozing): ")
            if student_name.lower() == 'stop':
                break
            file.write(student_name + '\n')  

add_students()

def get_students():
    try:
        with open('Students.txt', 'r') as file:
            students = file.readlines()
            for student in students:
                print(student.strip())  
    except FileNotFoundError:
        print("Fayl topilmadi.")

get_students() 
