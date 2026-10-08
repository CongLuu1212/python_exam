# main.py
from modules.functions import StudentManager

def main_menu():
    manager = StudentManager()
    
    while True:
        print("\n===== HỆ THỐNG QUẢN LÝ SINH VIÊN =====")
        print("1. Xem danh sách sinh viên")
        print("2. Thêm sinh viên mới")
        print("3. Xem sinh viên có điểm cao nhất")
        print("4. Xem điểm trung bình")
        print("5. Xem sinh viên đạt")
        print("6. Thoát chương trình")

        choice = input("Lựa chọn của bạn (1-6): ")

        if choice == '1':
            manager.show_all_students()
        elif choice == '2':
            manager.add_student()
        elif choice == '3':
            manager.student_highest_score()
        elif choice == '4':
            manager.average_score()
        elif choice == '5':
            manager.Student_who_passed()
        elif choice == '6':
            print("Đang thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại.")

if __name__ == "__main__":
    main_menu()
