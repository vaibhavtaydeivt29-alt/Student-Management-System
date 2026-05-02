import streamlit as st

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# -------------------- SESSION STATE --------------------
if "students" not in st.session_state:
    st.session_state.students = []


# -------------------- FUNCTIONS --------------------
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"


def add_student(name, roll, course, marks):
    grade = calculate_grade(marks)

    student = {
        "Name": name,
        "Roll No": roll,
        "Course": course,
        "Marks": marks,
        "Grade": grade
    }

    st.session_state.students.append(student)


def delete_student(roll):
    st.session_state.students = [
        student for student in st.session_state.students
        if student["Roll No"] != roll
    ]


# -------------------- UI --------------------
st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Student", "View Students", "Search Student", "Delete Student"]
)

# -------------------- ADD STUDENT --------------------
if menu == "Add Student":
    st.header("Add New Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    course = st.text_input("Course")
    marks = st.number_input("Marks", min_value=0, max_value=100)

    if st.button("Add Student"):
        if name and roll and course:
            add_student(name, roll, course, marks)
            st.success("Student Added Successfully!")
        else:
            st.warning("Please fill all fields")


# -------------------- VIEW STUDENTS --------------------
elif menu == "View Students":
    st.header("Student Records")

    if st.session_state.students:
        st.table(st.session_state.students)
    else:
        st.info("No student records found")


# -------------------- SEARCH STUDENT --------------------
elif menu == "Search Student":
    st.header("Search Student")

    search_roll = st.text_input("Enter Roll Number")

    if st.button("Search"):
        found = False

        for student in st.session_state.students:
            if student["Roll No"] == search_roll:
                st.success("Student Found")
                st.write(student)
                found = True
                break

        if not found:
            st.error("Student Not Found")


# -------------------- DELETE STUDENT --------------------
elif menu == "Delete Student":
    st.header("Delete Student")

    delete_roll = st.text_input("Enter Roll Number to Delete")

    if st.button("Delete"):
        delete_student(delete_roll)
        st.success("Student Deleted Successfully!")