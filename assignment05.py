# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Dominic Verretto, Aug 30, Writing Script for Assignment 4)
#   RRoot,1/1/2030,Created Script
#   <Dominic Verretto>,<Aug 30>, <Assignment 4>
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.csv"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: list = []  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
import csv
import json



# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    for row in file.readlines():# Transform the data from the file
        student_data = row.split(',')
        student_data = {"Student First Name":student_data[0], "Student Last Name":student_data[1], "Course Name":student_data[2].strip()}
        students.append(student_data)# Load it into our collection (list of lists)
    file.close()
except FileNotFoundError as e:
    print("This file does not exist! Trying to open it again after creating...")
    file = open(FILE_NAME, "w")
except Exception as e:
    print("There was an error opening the document")
    print(e, e.__doc__)



print(students)
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("Student First Name must consist of letters only")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Student Last Name must consist of letters only")
            course_name = input("Please enter the name of the course: ")
            student_data = {"Student First Name":student_first_name,"Student Last Name":student_last_name,"Course Name":course_name}
            students.append(student_data)
        except ValueError as e:
            print("Entry was not solely letters. Please try again.")
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student["Student First Name"]} {student["Student Last Name"]} is enrolled in {student["Course Name"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            for student in students:
                csv_data = f"{student["Student First Name"]}, {student["Student Last Name"]}, {student["Course Name"]}\n"
                file.write(csv_data)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student["Student First Name"]}, {student["Student Last Name"]} is enrolled in {student["Course Name"]}")
        except Exception as e:
            print("There was an error writing to the document")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
