class Course():
    def __init__(self, course_ID:str, course_name:str, course_type:str, course_fee:int):
        self.course_ID = course_ID
        self.course_name = course_name
        self.course_type = course_type
        self.course_fee = course_fee
        
    def get_course_info(self):
      return "Mã khóa học: " + self.course_ID + " - Tên khóa học: " + self.course_name + " - Hình thức học: " + self.course_type + " - Học phí: VND " + str(self.course_fee)


class Student():
    def __init__(self):
        self.student_ID:str =""
        self.student_name:str = ""
        self.student_DOB:str = ""
        self.course_list:list[Course] = []
        
    def input_data(self):
        self.student_ID = input("Nhập mã học viên: ")
        self.student_name = input("Nhập tên học viên: ")
        self.student_DOB = input("Nhập ngày sinh học viên: ")
       
    def register_course(self, course:Course):
        self.course_list.append(course) 
            
    def get_course_info(self):
        result = ""
        for course in self.course_list:
            result += course.get_course_info() + '\n'
        return result
            
    def display_student(self):
        print(f"Mã học viên: {self.student_ID} - Tên học viên: {self.student_name} - Ngày sinh: {self.student_DOB} - Khóa học đã đăng ký:\n{self.get_course_info()}")

    
course1 = Course("CS01", "CS Foudation", "Offline", 4000000)
course2 = Course("CS02", "CS Premium", "Online", 6000000)

print(course1.get_course_info())
print(course2.get_course_info())

student1 = Student()
student1.input_data()
student1.register_course(course1)
student1.register_course(course2)
student1.display_student()

student2 = Student()
student2.input_data()
student2.register_course(course2)
student2.display_student()
