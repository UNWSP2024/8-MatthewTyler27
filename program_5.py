#Matthew Tyler
#10/24/25
#Course Info

courses = {}

def course_info():

    while True:
        course_ID = input('Please enter course ID or "done" to finish.').strip()
        if course_ID.lower() == "done":
            break
        course_name = input("Enter course name: ").strip()
        #Adds Course name and ID to dictionary
        courses[course_ID] = course_name

#Call the function
course_info()
subject = input("Enter a subject to find classes (Example: COS). ").strip().upper()
#Iterates through all of courses
for course_ID, course_name in courses.items():
    #Finds courses with subject user entered
    if course_ID.upper().startswith(subject):
        print(course_ID, "-", course_name)
