# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Dominic Verretto, Sep, 3 2024, Assignment 6)
#   RRoot,1/1/2030,Created Script
#   <Dominic Verretto>,<Tue Sep 3>,<Modified Script for Assignment 6>
# ------------------------------------------------------------------------------------------ #
import json
from json import JSONDecodeError
from typing import TextIO


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
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file: TextIO = None  # Holds a reference to an opened file.
menu_choice: str  = '' # Hold the choice made by the user.


class FileProcessor:
    '''
    A collection of functions that manipulate the file.
    Dominic Verretto, Sep 3
    '''
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        global file
        global students
        '''
        Read data from a file.
        :param file_name:
        :param student_data:
        :return:
        '''
        try:
            file = open(FILE_NAME, "r")
            students = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("File not found", e)
        except JSONDecodeError as e:
            IO.output_error_messages("Invalid JSON", e)
        finally:
            if file.closed:
                file.close()

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        '''
        Write data to a file.
        :param file_name:
        :param students:
        :return:
        '''

        try:
            file = open(FILE_NAME, "a")

            # # JSON answer
            json.dump(students, file)

            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        except Exception as e:
            IO.output_error_messages("There was an error writing the data to the file", e)
        finally:
            if file.closed == False:
                file.close()



class IO:
    '''
    A collection of functions that involve user inputs
    Dominic Verretto, Sep 3
    '''
    @staticmethod
    def output_error_messages(message: str, exception: Exception = None):
        print(message)
        if exception is not None:
            print('--Technical Information--')
            print(exception, exception.__doc__, type(exception), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        return print(menu)

    @staticmethod
    def input_menu_choice():
        print(MENU)
        menu_choice = input("What would you like to do: ")
        while menu_choice not in ['1', '2', '3', '4']:
            IO.output_error_messages("Invalid choice, enter a number between 1 and 4")
            menu_choice = input(MENU)
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("Input must be alphabetical", e)
        except Exception as e:
            IO.output_error_messages("There was an error with your input. Please try again", e)


FileProcessor.read_data_from_file(FILE_NAME, student_data)
while (True):
    menu_choice = IO.input_menu_choice()
 # Input user data
    if menu_choice == "1":
        IO.input_student_data(student_data)
        continue
    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, student_data)
        continue
    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3,or 4")

print("Program Ended")


