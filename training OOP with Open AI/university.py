class University:
    def __init__(self, name, location):
        self.name = str(name)
        self.location = str(location)
        self.programs = {}
        self.students = {}
        self.faculty = {}

    def add_program(self, program_name, program_details):
        self.programs[program_name] = program_details
        return self.programs

    def remove_program(self, program_name):
        self.programs[program_name] = None

    def add_student(self, student_name, student_details):
        self.students[student_name] = student_details

    def remove_student(self, student_name):
        self.students[student_name] = None

    def add_faculty(self, faculty_name, faculty_details):
        self.faculty[faculty_name] = faculty_details

    def remove_faculty(self, faculty_name):
        self.faculty[faculty_name] = None

    def __str__(self):
        program_str = "\n".join(
            [f" - {name} (degree : {details['degree']}, duration : {details['duration']})" for name, details in
             self.programs.items()])
        student_str = "\n".join(
            [f" - {name} (program : {details['program']}, year : {details['year']})" for name, details in
             self.students.items()])
        faculty_str = "\n".join(
            [f" - {name} (department : {details['department']})" for name, details in self.faculty.items()])
        return f"{self.name} in {self.location}\nOffers the following programs:\n{program_str}\n" \
               f"Students:\n{student_str}\nFaculty:\n{faculty_str}"


'''The __str__() it still iterates over the items of the dictionary, but it directly uses the python items() method.
 It also directly uses the keys of the dictionaries to access the details, by just calling the keys of the dictionary, 
 like details['degree']

This version may be a bit more readable and avoids the nested for loops and indexing, but it achieves the same result.
Please let me know if you have any question, or if there is anything else I can help you with.'''

university = University("OpenAI University", "San Francisco")
university.add_program("Computer Science", {"degree": "BSc", "duration": 4})
university.add_program("Robotics", {"degree": "MSc", "duration": 2})
university.add_student("Alice", {"program": "Computer Science", "year": 2})
university.add_student("Bob", {"program": "Robotics", "year": 1})
university.add_faculty("Dr. Jane Smith", {"department": "Computer Science"})
university.add_faculty("Dr. John Doe", {"department": "Robotics"})

print(university)
# OpenAI University in San Francisco
# Offers the following programs:
#   - Computer Science (BSc, 4 years)
#   - Robotics (MSc, 2 years)
# Students:
#   - Alice (Computer Science, year 2)
#   - Bob (Robotics, year 1)
# Faculty:
#   - Dr. Jane Smith (Computer Science)
#   - Dr. John Doe (Robotics)


'''Create a class called University that has the following instance variables:

name (str) : name of the university
location (str) : location of the university
programs (list of dict) : list of programs offered by the university
students (list of dict) : list of students in the university
faculty (list of dict) : list of faculties in the university
The class should have the following methods:

__init__(self, name, location) : This is the constructor for the class. It should initialize the name and location
instance variables.
add_program(self, program_name, program_details) : This method should add a new program to the university.
The program_name should be added to the list of programs as key and program_details as value in the dictionary.
remove_program(self, program_name) : This method should remove a program from the university.
add_student(self, student_name, student_details) : This method should add a new student to the university.
The student_name should be added to the list of students as key and student_details as value in the dictionary.
remove_student(self, student_name) : This method should remove a student from the university.
add_faculty(self, faculty_name, faculty_details) : This method should add a new faculty to the university.
The faculty_name should be added to the list of faculties as key and faculty_details as value in the dictionary.
remove_faculty(self, faculty_name) : This method should remove a faculty from the university.
__str__(self) : This method should return a string representation of the university with all its programs,
students, and faculties.'''
