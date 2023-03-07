# This is a student management application
# Parameters
# Student login
# gets verified,Check courses,check lecturers
# Admin login
# Add student, remove student, check if a student exists,etc

import random
from admin import Admin, student
import os
from time import sleep
import csv



# Create a function that generates a random reference number for each student
def generate_ref():
    list_of_numbers = "0123456789"
    ref = ""
    for i in range(8):
        ref += random.choice(list_of_numbers)
    return ref

# Create a function that generates a random index number for each student
def generate_index():
    list_of_numbers = "0123456789"
    index_no = ""
    for i in range(7):
        index_no += random.choice(list_of_numbers)
    return index_no

def admin_login(admin_name,admin_id):

    # create an instance of the admin class
    admin = Admin(admin_name,admin_id)

    # check if the admin details exist in the admin data base
    if (admin_name in admin.admin_name) and (admin_id in admin.admin_ids):
        os.system("cls")
        # Now that the login is successful go ahead and display the functionalities an admin can perform
        print("[1] Add new student")
        sleep(.5)
        print("[2] Remove student")
        sleep(.5)
        print("[3] Print the entire database")
        sleep(.5)
        print("[4] search for a student")
        sleep(.5)
        print("[5] Check total number of students")
        sleep(.5)
        print("[6] Go to Main Menu")
        sleep(.5)

        option = int(input(">>> "))
        os.system("cls")
        if option == 1:
            # option 1 allows the admin to add a new student to the database taking their details
            student_name = input("Enter student's name: ")
            student_program = input("Enter student's program: ")
            student_level = input("Enter student's level/year: ")
            student_reference = generate_ref()
            student_index_no = generate_index()

            # open the csv file and check if the index number and reference autogenerated do not already exist
            with open("student_Database.csv","r",newline="") as SDB:
                csv_reader = csv.reader(SDB,delimiter="\t")
                for line in csv_reader:
                    if student_reference == line[0] and student_index_no == line[1]:
                        student_reference = generate_ref()
                        student_index_no = generate_index()
                    else:
                        continue

            admin.add_student(student_name,student_reference,student_index_no,student_program,student_level)
            print("Student added successfully")
            input("Press enter to continue")
            return admin_login(admin_name,admin_id)
        elif option == 2:
            # option 2 allows the admin to remove a student from the DB
            os.system("cls")
            reference_number = input("Enter reference number of student to remove: ")
            admin.remove_student(reference_number)
            
            input("Press enter to continue")
            return admin_login(admin_name,admin_id)

        elif option == 3:
            # Option 3 allows the admin to print the student DB
            os.system("cls")
            admin.print_student_DB()
            input("Press enter to continue")
            return admin_login(admin_name,admin_id)
        elif option == 4:
            # option 4 allows the admin to search for a student using their reference numbers
            os.system("cls")
            # ask for the reference number of the student 
            reference_number = input("Enter student reference number: ")

            # pass the reference number as a parameter for the admin.search_student() method
            admin.search_student(reference_number)

            input("Press enter to continue")
            return admin_login(admin_name,admin_id)
        elif option == 5:
            # the user choses option 5 then the admin will be able to check the total number of students in the DB
            os.system("cls")
            admin.total_no_students()

            input("Press enter to continue")
            return admin_login(admin_name,admin_id)
        elif option == 6:
            # Option 6 returns the user to the main menu
            return
        else:
            # If the user enters the wrong input he/she is allow to try again
            print("Wrong Input!")
            return admin_login(admin_name,admin_id)

    else:
        print("Wrong Admin details")
        input("Press enter to retry!")
        os.system("cls")
    
# All functionalities that a student can perform are in this function
def student_login(reference_no,index_no):

    # create an instance of the students class
    student1 = student(reference_no,index_no)

    # validate student => the students reference number and index number is taken to validate them
    validate = student1.validate_student(reference_no,index_no)
    if validate == True:
        os.system("cls")
        print("[1] View courses and lecturers")
        option = int(input(">>> "))
        if option == 1:
            os.system("cls")

            #print the courses and lecturers of the student
            student1.CL()
            input("Press enter to return to the main menu")
            os.system("cls")
    else:
        os.system("cls")
        print("Wrong student details!")
        input("Press enter to try again")


# the main function
def main():
    is_true = True

    # main program loop
    while is_true:
        print("\n")
        print("\t\t      COE2 STUDENTS' MANAGEMENT SYSTEM       \n")
        print("========================================================")
        sleep(.5)
        print("login As: ")
        sleep(.5)
        print("[1] Student")
        sleep(.5)
        print("[2] Admin")
        sleep(.5)
        print("[3] Exit")

        # accept response from the user
        user_response = int(input(">>> "))
        if user_response == 1:
            
            os.system("cls")
            # ask the student for their index number and reference number
            reference = input("Enter Reference number: ")
            index_number = input("Enter index number: ")

            # pass the arguments to the student
            student_login(reference,index_number)

        elif user_response == 2:
            os.system("cls")
            # ask for admin details
            admin_name = input("Name:")
            admin_id = input("Password: ")
            admin_login(admin_name,admin_id)
        elif user_response == 3:
            os.system("cls")
            print("Thank you for using Student Management System")
            is_true = False
        else:
            print("Invalid Response!")
            os.system("cls")
            input("Press enter to retry!")

main()

