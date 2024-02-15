# For this portion, we will work together. 
# Please follow along with the teacher. Please do not to work ahead.


# Let's say we want to have some student records in our program
student_1_id = 18584831
student_1_first_name = "Daniel"
student_1_last_name = "White"
student_1_major = "Computer Science"
student_1_expected_graduation_year = "2026"

student_2_id = 18582185
student_2_name = "Jennie"
student_2_last_name = "Kim"
student_2_major = "Chemistry"
student_2_expected_graduation_year = "2025"

# TODO: Create a new student student_3 following the same format
student_3_id = 98463728
student_3_first_name = "Adam"
student_3_last_name = "Mooney"
student_3_major = "Computer Science"
student_3_expected_graduation_year = "2025"

# Discussion: What are some problems with this approach?
'''
The student data needs to be stored collectively instead of individually. Perhaps creating a class called 'student_info' that stores data for each student within the same array.
'''

# OOP Property - Encapsulation: Let's contain all of this data into a single Student class


# Basic structure of a class
class Student:
    # TODO: Let's build this class!
    def __init__(self, id, first_name, last_name, major, grad_year):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.grad_year = grad_year
        pass

        @property
        def id(self):
         self.__id

        def get_full_name(self):
            return str(self.first_name, self.last_name)
        
        def print_degree_title(self):
            print("Bachelor of " + self.major + "with a specialization in " + self.specialization)


# TODO: Let's recreate our 3 students as objects of our new class!

student_1 = Student(18584831, "Daniel", "White", "Computer Science", "2026")
student_2 = Student(98463728, "Jennie", "Kim", "Chemistry", "2025")
Student_3 = Student(98463728, "Adam", "Mooney", "Political Science", "2025")


# OOP Property Abstraction: The idea of making certain data private
# This prevents other functions/parts of the code from accessing or modifying a value.
    
# TODO: Make the id private.
# Test your code and ensure you cannot access student_1.__id (you should see an error)
#print(student_1.__id)

# This is good because it prevents users from modifying the id by accident.
# However, what if they need to see the id?
    
# TODO: Add an @property getter for id
# Test to make sure you can get the id with student_1.id
    
@property
def id(self):
    return self.student_1.__id

# What if we want a way to just get the last four of the id instead of the whole thing? We can build a custom class method to do this.
    
# Create a method in the class called get_last_four
# This should return the last four numbers of the id.
    
def get_last_four(self):

    return int(str(self.__id)[-4:])



# OOP Property - Inheritence:
# A class can inherit from another class.
# The inheriting class is known as a child class
# The class inherited from is known as the parent class
    
# TODO: Create a child class called GradStudent which inherits from the Student class, with the additional property of "specialization"

class gradstudent(Student):
    def __init__(self, id, first_name, last_name, major, grad_year, specialization):
        super().__init__(id, first_name, last_name, major, grad_year)
        self.specialization = specialization

# create a new student_4 which uses GradStudent instead.
# this person's major is Computer Science and their Specialization is Artifical Intelligence
student_4_id = 18582098
student_4_name = "Jim"
student_4_last_name = "Tim"
student_4_major = "Biology"
student_4_expected_graduation_year = "2025"

student_4 = gradstudent(18582098, "Jim", "Tim", "Biology", "2025", "bio stuff")
print(gradstudent)

# OOP Property - Polymorphism
# refers to methods/functions/operators with the same name that can be executed on many objects or classes.
    
# for example, maybe we want a method called print_degree_title, which will print "Bachelor of {major}".
# TODO: add the print_degree_title method to the Student class
print(student_1.print_degree_title)
# What happens if we run student_4.print_degree_title?
# Yes, it will print "Bachelor of Computer Science".
    
# This is not what we want though, because it should print Master of Computer Science for our graduate school student. 
    
# We can override our parent method in the child class by creating a function with the exact same name: print_degree_title
    
# TODO: Add the print_degree_title to the Graduate class, have it print "Master of {major} with a specialization in {specialization}."
def print_degree_title(self):
     print("Master of " + self.major + "with a specialization in " + self.specialization)

# Test your code and make sure print_degree_title prints the master's student as intended.
    
# This is the end of the OOP lesson. Look at part_2.py for the follow up to this lesson. 
    


