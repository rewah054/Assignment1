class CourseManagementClass:
    courses_list = []
    list_of_student_names = []
    master_student_course_enrolment_dictionary = {}
    master_student_grade_list = {}

    def __init__(self):
        pass

    def add_course(self):

        new_course = input("What is the name of the new course?: ").title()
        while True:

            if new_course.title() not in self.courses_list:
                self.courses_list.append(new_course.title())

            else:
                print(f"The course {new_course.title()} is already on the list")

            done = input("Enter a new course or press 'q' to quit: ").title()
            if done == 'Q':
                print(f"The course list includes: {self.courses_list}")
                break
            else:
                new_course = done

    def modify_course_list(self):
        """
        replace one course with another
        :return:
        """
        course_to_modify = input("Which course will you like to modify?: ").title()
        if course_to_modify not in self.courses_list:
            print(f"{course_to_modify} is not in the course list")
        else:
            replacement_course = input("What is the name of the replacement course?: ")
            i = self.courses_list.index(course_to_modify)
            self.courses_list = self.courses_list[:i] + [replacement_course] + self.courses_list[i + 1:]

        print(f"The current course list includes: {self.courses_list}")

    def delete_course(self):
        course_to_delete = input("Which course will you like to delete?: ").title()
        while True:

            if course_to_delete.title() not in self.courses_list:
                print(f"The course {course_to_delete} is not on the course list")
            else:
                self.courses_list.remove(course_to_delete)
                print(f"The course {course_to_delete} has been deleted!")

            done = input("Enter a new course or press 'q' to quit: ").title()
            if done == 'Q':
                print(f"The course list includes: {self.courses_list}")
                break
            else:
                course_to_delete = done

    def get_course_list(self):
        return self.courses_list

    # Add student
    def add_student(self):

        new_student_name = input("Enter the name of the student you will like to add: ").title()
        while True:
            if new_student_name.title() not in self.list_of_student_names:
                self.list_of_student_names.append(new_student_name.title())
            else:
                print(f"{new_student_name} is already a student")

            done = input("Enter a new student name or press 'q' to quit: ").title()
            if done == 'Q':
                print(f"The list of students includes: {self.list_of_student_names}")
                break
            else:
                new_student_name = done

    # Modify student - change student name
    def modify_student(self):
        """
        rename student name list (delete old student, replace them with new student)
        :return:
        """
        student_to_modify = input("Which student will you like to modify?: ").title()
        if student_to_modify not in self.list_of_student_names:
            print("Your student is not in the student list")
        else:
            replacement_student = input("What is the name of the replacement student?: ").title()
            i = self.list_of_student_names.index(student_to_modify)
            self.list_of_student_names = self.list_of_student_names[:i] + [
                replacement_student] + self.list_of_student_names[i + 1:]

        print(f"The current student list includes: {self.list_of_student_names}")

    # Delete student
    def delete_student(self):
        student_to_delete = input("Which student will you like to delete?: ").title()
        while True:
            if student_to_delete.title() not in self.list_of_student_names:
                print(f"The student {student_to_delete} is not on the student list")
            else:
                self.list_of_student_names.remove(student_to_delete)
                print(f"The student {student_to_delete} has been deleted!")

            done = input("Enter a new course or press 'q' to quit: ").title()
            if done == 'Q':
                print(f"The student list includes: {self.list_of_student_names}")
                break
            else:
                student_to_delete = done

        print(f"The current student list includes: {self.list_of_student_names}")

    def get_student_list(self):
        return self.list_of_student_names

    def enrol_students(self):
        self.courses_list = self.get_course_list()
        self.list_of_student_names = self.get_student_list()
        student_course_list = []

        student_to_enrol = input("What is the name of the student you will like to enrol in courses?: ").title()

        if student_to_enrol.title() not in self.list_of_student_names:
            print(f"{student_to_enrol.title()} has to be added first before they can be enrolled in courses!")
        else:
            student_enrolment_course = input("Which course will you like to enrol in?: ").title()

            while True:
                if student_enrolment_course.title() not in self.courses_list:
                    print(f"{student_enrolment_course} is not on the course list. Add the course first!")
                else:
                    student_course_list.append(student_enrolment_course)
                    print(f"{student_enrolment_course} has been added to {student_to_enrol}'s course list!")

                done = input("Enter a new course or press 'q' to quit: ").title()
                if done == 'Q':
                    self.master_student_course_enrolment_dictionary[student_to_enrol.title()] = student_course_list
                    print(f"{student_to_enrol}'s course list includes: {student_course_list}")
                    break
                else:
                    student_enrolment_course = done

    def unenrol_students(self):
        student_to_unenrol = input("What is the name of the student you will like to unenrol from courses?: ").title()

        if student_to_unenrol.title() not in self.get_master_student_course_enrolment_dictionary().keys():
            print(f"{student_to_unenrol.title()} has to be added and enrolled before they can be unenrolled!")
        else:
            student_current_enrolment_list = self.get_master_student_course_enrolment_dictionary()[
                student_to_unenrol.title()]
            course_to_unenrol = input("Which course will you like to unenrol from?: ").title()

            while True:
                if course_to_unenrol.title() not in student_current_enrolment_list:
                    print(f"The student is currently not enrolled in the {course_to_unenrol.title()} course!")
                else:
                    student_current_enrolment_list.remove(course_to_unenrol.title())
                    print(f"{student_to_unenrol.title()} has been unenrolled from {course_to_unenrol.title()}!")

                done = input("Enter a new course or press 'q' to quit: ").title()
                if done == 'Q':
                    self.master_student_course_enrolment_dictionary[
                        student_to_unenrol.title()] = student_current_enrolment_list
                    print(f"{student_to_unenrol}'s updated course list includes: {student_current_enrolment_list}")
                    break
                else:
                    course_to_unenrol = done

    def get_master_student_course_enrolment_dictionary(self):
        return self.master_student_course_enrolment_dictionary

    def submit_grade(self):
        """
        This function allows the Admin to submit grades for students
        More stringent checks can be put in place here but this version does the basic functionality needed
        :return:
        """

        student_to_be_graded = input("Which student will you like to submit grades for?: ").title()

        while True:
            if student_to_be_graded not in self.get_master_student_course_enrolment_dictionary().keys():
                print(f"{student_to_be_graded} has to be added and enrolled before their grades can be submitted!")
            else:
                student_current_enrolment_list = self.get_master_student_course_enrolment_dictionary()[
                    student_to_be_graded]

                print(f"{student_to_be_graded}'s courses include: {student_current_enrolment_list}")

                grade_list = []
                for courses in student_current_enrolment_list:
                    grade = input(f"What is {student_to_be_graded}'s grade for {courses}?: ").title()
                    grade_list.append(grade)

                self.master_student_grade_list[student_to_be_graded] = [student_current_enrolment_list, grade_list]

            done = input("Enter a new student name to be graded or press 'q' to quit: ").title()
            if done == 'Q':
                print(f"The grades for all the students includes: {self.master_student_grade_list}")
                break
            else:
                student_to_be_graded = done

    def get_students_grade_list(self):
        return self.master_student_grade_list


    # Enrol students - add student to specific course(s)
    # Unenrol students - remove student from specific course(s)
    # Submit grade
