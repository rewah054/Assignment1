from CourseManagement import CourseManagementClass
from Student import StudentClass


def assignment():
    """
    We will authenticate the admin with a made up username/password
    We want Admin to add some students
    We want Admin to add some courses
    We want Admin to enrol some students in certain classes
    We want Admin to unenrol one student
    We want Admin to submit student grades for two students
    We want one student to add/modify/delete courses
    :return:
    """
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    if username.title() == "Admin" and password == "12345":
        print("Welcome Admin! Have a good day!!")
        Admin = CourseManagementClass()
        Admin.add_student()
        Admin.add_course()

        Admin.enrol_students()
        Admin.enrol_students()
        Admin.enrol_students()

        Admin.unenrol_students()

        Admin.submit_grade()

        Admin.get_students_grade_list()

        student_authentication = input("Are you a student?: (Enter Y or y)").title()
        if student_authentication == "Y":
            student_name = input("What is your student name?").title()
            if student_name not in Admin.list_of_student_names:
                print(f"{student_name}, you are not enrolled in any course!")
            else:
                student_course_list = Admin.get_master_student_course_enrolment_dictionary()["Roseline"]
                master_course_list = Admin.get_course_list()

                Student_object = StudentClass(student_name, student_course_list, master_course_list)
                Student_object.student_add_course()
                Student_object.student_modify_course_list()
                Student_object.student_delete_course()

        else:
            print("Logging off Admin!")
    else:
        print("You need to be a student or an Admin to use this system!")


if __name__ == '__main__':
    assignment()
