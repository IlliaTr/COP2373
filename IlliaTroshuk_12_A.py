import numpy as np
import csv

# Load the data from the CSV file
def load_data(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip header
        data = []
        for row in reader:
            data.append(row[2:])  # Take only exam scores
    return np.array(data, dtype=int)

# Print the first few rows of the dataset
def print_first_rows(data, num_rows=5):
    print("First few rows of the dataset:")
    print(data[:num_rows])

# Calculate and print statistics for each exam
def calculate_exam_statistics(data):
    print("\nExam Statistics:")
    num_exams = data.shape[1]
    for n in range(num_exams):
        exam_scores = data[:, n]
        print(f"Exam {n+1}:")
        print(f"    Mean: {np.mean(exam_scores):.2f}")
        print(f"    Median:: {np.median(exam_scores):.2f}")
        print(f"    Standard Deviation: {np.std(exam_scores):.2f}")
        print(f"    Minimum: {np.min(exam_scores)}")
        print(f"    Maximum: {np.max(exam_scores)}")

# Calculate and print overall statistics for all exams combined
def calculate_overall_statistics(data):
    all_scores = data.flatten()
    print("\nOverall statistics for all exams combined:")
    print(f"    Mean: {np.mean(all_scores):.2f}")
    print(f"    Median: {np.median(all_scores):.2f}")
    print(f"    Standard Deviation: {np.std(all_scores):.2f}")
    print(f"    Minimum: {np.min(all_scores)}")
    print(f"    Mamimum: {np.max(all_scores)}")

# Determine and print the number of students who passed and failed each exam
def pass_fail_statistics(data, passing_grade=60):
    num_exams = data.shape[1]
    for n in range(num_exams):
        exam_scores = data[:, n]
        passed = np.sum(exam_scores >= passing_grade)
        failed = np.sum(exam_scores < passing_grade)
        print(f"\nExam {n+1}:")
        print(f"    Passed: {passed}")
        print(f"    Failed: {failed}")

# Calculate and print the overall pass percentage across all exams
def overall_pass_percentage(data, passing_grade=60):
    total_students = data.shape[0] * data.shape[1]
    passed_students = np.sum(data >= passing_grade)
    pass_percentage = (passed_students / total_students) * 100
    print(f"\nOverall pass percentage: {pass_percentage:.2f}%")

# Main function to run all tasks
def main():
    filename = 'grades.csv'
    data = load_data(filename)
    print_first_rows(data)
    calculate_exam_statistics(data)
    calculate_overall_statistics(data)
    pass_fail_statistics(data)
    overall_pass_percentage(data)

if __name__ == '__main__':
    main()