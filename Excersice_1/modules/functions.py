from models.student import Student

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        print("\n--- Thêm Sinh Viên Mới ---")
        sid = input("Nhập mã sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        score = float(input("Nhập điểm python: "))
        
        new_student = Student(sid, name, score)
        self.students.append(new_student)
        print("Thêm sinh viên thành công!")

    def show_all_students(self):
        print("\n--- Danh Sách Sinh Viên ---")
        if not self.students:
            print("Danh sách trống.")
        else:
            for st in self.students:
                print(st)
                input("Nhấn Enter để tiếp tục...")

    def student_highest_score(self):
        if not self.students:
            print("Danh sách trống.")
            return
        highest = max(self.students, key=lambda st: st.score)
        print("\n--- Sinh Viên Có Điểm Cao Nhất ---")
        print(highest)
        input("Nhấn Enter để tiếp tục...")

    def average_score(self):
        if not self.students:
            print("Danh sách trống.")
            return
        total = sum(st.score for st in self.students)
        average = total / len(self.students)
        print(f"\n--- Điểm Trung Bình ---")
        print(f"Điểm trung bình: {average:.2f}")
        input("Nhấn Enter để tiếp tục...")

    def Student_who_passed(self):
        print("\n--- Danh Sách Sinh Viên Đạt ---")
        passed_students = [st for st in self.students if st.score >= 5]
        if not passed_students:
            print("Không có sinh viên nào đạt.")
        else:
            for st in passed_students:
                print(st)
                input("Nhấn Enter để tiếp tục...")