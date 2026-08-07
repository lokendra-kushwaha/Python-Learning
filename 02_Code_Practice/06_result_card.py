"""
Topic: Basic Output Formatting and Arithmetic Operations
Goal: To generate a formatted report card using print() parameters like 'sep' and 'end' for spatial alignment.
"""

# Student Details
student_name = "Lokendra Kushwaha"
age = 20
exam_name = "UPSC/SSC"
rollnumber = 8188916838

# Subject Marks
history = 96
geography = 90
polity = 93

# Calculations
TotalMarks = 300
TotalObt = history + geography + polity
Percentage = TotalObt * 100 / 300

# Displaying Header Information
# Using 'end' parameter to prevent automatic new lines and add custom spacing instead
print("Name - ", student_name, end="                                                              ")
print("Age - ", age, end="                                                                 ")
print("Exam", exam_name, end="                                                                          ")
print("Roll Number - ", rollnumber)

# Displaying Marks Table
# Using 'sep' (separator) parameter to create uniform column gaps between multiple arguments
print("Subject", "Total Max.", "Total Min.", "Total Obt.", sep="                                      ")
print("History  ", 100, 33, history, sep="                                           ")
print("Geography", 100, 33, geography, sep="                                           ")

# Printing the last subject and appending the final percentage at a specific distance
print("Polity   ", 100, 33, polity, sep="                                           " , end="                                                                                                                                                 ") 

print("Percentage - ", Percentage, "%")