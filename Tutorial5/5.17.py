import pandas as pd

# Read the CSV file
student_df = pd.read_csv("student.csv")

# 1) Find the average CGPA of all students
avg_cgpa = student_df["CGPA"].mean()
print("Average CGPA of Students:", round(avg_cgpa, 2))

# 2) Display details of students with CGPA > 9
top_cgpa_students = student_df[student_df["CGPA"] > 9]
print("\nStudents with CGPA > 9:\n", top_cgpa_students)

# 3) Display details of CSE students with CGPA > 9
cse_top_students = student_df[(student_df["Branch"] == "CSE") & (student_df["CGPA"] > 9)]
print("\nCSE Students with CGPA > 9:\n", cse_top_students)

# 4) Display details of the student with the maximum CGPA
highest_cgpa_student = student_df[student_df["CGPA"] == student_df["CGPA"].max()]
print("\nStudent with Maximum CGPA:\n", highest_cgpa_student)

# 5) Display average CGPA of each branch
avg_cgpa_by_branch = student_df.groupby("Branch")["CGPA"].mean()
print("\nAverage CGPA of Each Branch:\n", avg_cgpa_by_branch)
