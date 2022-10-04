from CourseManagement import CourseManagementClass


class StudentClass:
    """
    The student class allows the student to add courses to existing course list, modify course list, and delete courses.
    Other tasks have to be done by the Admin
    """

    def __init__(self, name, student_course_list, master_course_list):
        self.name = name
        self.student_course_list = student_course_list
        self.master_course_list = master_course_list

    # def enrol_in_course (self):

    def student_add_course(self):
        print(f"The list of all the courses available includes: {self.master_course_list}")
        print(f"The list of all the courses you are enrolled in includes: {self.student_course_list}")

        new_course = input("What is the name of the new course you will like to add?: ").title()

        while True:
            if new_course not in self.master_course_list:
                print(f"{new_course} does not exist! You can only add a course that has been made available by the "
                      f"Admin")
            elif new_course in self.student_course_list:
                print(f"You are already enrolled in {new_course}!")
            elif new_course in self.master_course_list and new_course not in self.student_course_list:
                self.student_course_list.append(new_course)
                print(f"{new_course} has been added to your course list")

            done = input("Enter a new course or press 'q' to quit: ")

            if done == 'q' or done == 'Q':
                print(f"The course list includes: {self.student_course_list}")
                break
            else:
                new_course = done

    def student_modify_course_list(self):
        print(f"The list of all the courses available includes: {self.master_course_list}")
        print(f"The list of all the courses you are enrolled in includes: {self.student_course_list}")

        course_to_modify = input("What is the name of the new course you will like to modify?: ").title()
        if course_to_modify not in self.student_course_list:
            print(f"{course_to_modify} is not on your course list")
        elif course_to_modify not in self.master_course_list:
            (f"{course_to_modify} does not exist! You can only modify a course that has been made available by the "
             f"Admin")
        elif course_to_modify not in self.student_course_list and course_to_modify in self.master_course_list:
            replacement_course = input("What is the name of the replacement course?: ")
            i = self.student_course_list.index(course_to_modify)
            self.student_course_list = self.student_course_list[:i] + [replacement_course] + \
                                       self.student_course_list[i + 1:]

        print(f"Your current course list includes: {self.student_course_list}")

    def student_delete_course(self):
        course_to_delete = input("Which course will you like to delete?: ").title()
        while True:

            if course_to_delete not in self.student_course_list:
                print(f"The {course_to_delete} - course is not on the course list")
            elif course_to_delete not in self.master_course_list:
                (f"{course_to_delete} does not exist! You can only delete a course that has been made available by the "
                 f"Admin")
            else:
                self.student_course_list.remove(course_to_delete)
                print(f"The course {course_to_delete} has been deleted!")

            done = input("Enter another course to be deleted or press 'q' to quit: ")
            if done == 'q' or done == 'Q':
                print(f"The course list includes: {self.student_course_list}")
                break
            else:
                course_to_delete = done
