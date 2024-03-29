class Student:
    def _init_(self):
        self.scores = [0] * 5
    

    def input_scores(self):
        self.scores = list(map(int, input().split()))

    def calculate_total_score(self):
        return sum(self.scores)


# Main program
def main():
    # Input the number of students
    num_students = int(input("Enter the number of students: "))

    # Input Kristen's scores
    kristen = Student()
    print("Enter Kristen's scores:")
    kristen.input_scores()
    kristen_score = kristen.calculate_total_score()

    # Count the number of students who scored higher than Kristen
    count_higher = 0
    for _ in range(num_students - 1):  # Subtract 1 for Kristen
        student = Student()
        print(f"Enter scores for student {_ + 1}:")
        student.input_scores()
        if student.calculate_total_score() > kristen_score:
            count_higher += 1

    # Output the result
    print(f"Number of students who scored higher than Kristen: {count_higher}")


