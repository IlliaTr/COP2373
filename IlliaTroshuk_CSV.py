# Recording Student's Exam Scores

import csv

# Function to write student grades to a CSV file
def write_grades():
    # Collecting the number of students
    num_students = int(input("Please enter the number of students: "))

    # File name
    filename = 'grades.csv'

    # Opening the CSV file in write mode
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Writing the header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Collecting and writing each student's data
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam1 = int(input("Enter the score for Exam 1: "))
            exam2 = int(input("Enter the score for Exam 2: "))
            exam3 = int(input("Enter the score for Exam 3: "))
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print(f"\nData has been written to {filename}")

# Run the function
if __name__ == '__main__':
    write_grades()

# Function to read student grades from a CSV file and display them
def read_grades():
    filename = 'grades.csv'

    # Reading the CSV file
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Reading the header

        # Printing the header
        print(f"\n{header[0]:<15} {header[1]:<15} {header[2]:<10} {header[3]:<10} {header[4]:<10}")

        # Printing each row of student data
        for row in reader:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<10} {row[3]:<10} {row[4]:<10}")

# Run the function
if __name__ == '__main__':
    read_grades()
