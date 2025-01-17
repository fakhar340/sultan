class Exams():
    def __init__(self, student_name, student_rollNumber, obtain_marks, total_marks, subject, date):
        self.student_name = student_name
        self.student_rollNumber = student_rollNumber
        self.obtain_marks = obtain_marks  
        self.total_marks = total_marks 
        self.subject = subject
        self.date = date        
        self.percentage = (self.obtain_marks / self.total_marks) * 100  

    def get_exam(self):
        return f"Student Name: {self.student_name},\nStudent Roll Number: {self.student_rollNumber},\nObtain Marks: {self.obtain_marks},\nTotal Marks: {self.total_marks},\nSubject: {self.subject},\nDate: {self.date},\nPercentage: {self.percentage:.2f}%"
