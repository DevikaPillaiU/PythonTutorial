import pandas as pd

def save_student_marks():
    student_data = {
        "Reg_no": [10001, 10002, 10003],
        "Name": ["Jack", "John", "Alex"],
        "Sub_Mark1": [76, 77, 74],
        "Sub_Mark2": [88, 84, 79],
        "Sub_Mark3": [76, 79, 81]
    }

    marks_df = pd.DataFrame(student_data)

    marks_df.to_csv("student_marks.csv", index=False)

    print("Data successfully written to student_marks.csv!")

save_student_marks()
