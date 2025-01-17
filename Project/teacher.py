class Teacher():
    def __init__(self,
        teacher_name,
        teacher_f_name,
        teacher_phone_name,
        teacher_salary,         
        ):
        self.teacher_name = teacher_name
        self.teacher_f_name = teacher_f_name
        self.teacher_phone_number = teacher_phone_name
        self.teacher_salary = teacher_salary

    def getteacher(self):
        return f" Name: {self.teacher_name}  Father Name: {self.teacher_f_name} Phone Number: {self.teacher_phone_number}"   
