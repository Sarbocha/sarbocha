import tkinter as tk
import csv

root = tk.Tk()
root.title("APP BY SARBOCHA")


def submit():
    global dictionary
    with open("file", "w") as file:
        titles = ["Name", "Grade", "Roll No"]
        csv_writer = csv.DictWriter(file, fieldnames=titles)
        csv_writer.writeheader()
        csv_writer.writerow({"Name": name, "Grade": classes, "Roll No": roll })
        file.write("\n")
        csv_writer.writerow({"Name": name, "Grade": classes, "Roll No": roll})

def repeat():
    global name_var
    global grade_var
    global roll_var
    name_entry = tk.Entry(root, text="Your Name:", textvariable=name_var, width=40, borderwidth=10)
    name_entry.grid(row=0, column=1, padx=50, pady=20)
    name_entry.delete(0, "end")

    grade = tk.Entry(root, text="Your Grade", textvariable=grade_var, width=40, borderwidth=10)
    grade.grid(row=1, column=1, padx=50, pady=20)
    grade.delete(0, "end")

    roll_no = tk.Entry(root, text="Your Roll No", textvariable=roll_var, width=40, borderwidth=10)
    roll_no.grid(row=2, column=1, padx=50, pady=20)
    roll_no.delete(0, "end")


def done():
    global name
    global classes
    global roll
    name = name_var.get()
    classes = str(grade_var.get())
    roll = str(roll_var.get())


def check():
    if len(name) <= 50:
        pass

    else:
        name_entry.insert(0, "Invalid Name")
        return 1

    if classes > 13:
        grade.insert(0, "Invalid Grade!")
        return 1
    else:
        pass

    if roll > 100:
        roll_no.insert(0, "Invalid Roll No")
        return 1
    else:
        pass


name_var = tk.StringVar()
grade_var = tk.IntVar()
roll_var = tk.IntVar()

name_entry = tk.Entry(root, text="Your Name:", textvariable=name_var, width=40, borderwidth=10)
name_entry.grid(row=0, column=1, padx=50, pady=20)
name_entry.delete(0, "end")

grade = tk.Entry(root, text="Your Grade", textvariable=grade_var, width=40, borderwidth=10)
grade.grid(row=1, column=1, padx=50, pady=20)
grade.delete(0, "end")

roll_no = tk.Entry(root, text="Your Roll No", textvariable=roll_var, width=40, borderwidth=10)
roll_no.grid(row=2, column=1, padx=50, pady=20)
roll_no.delete(0, "end")

check_value_button = tk.Button(root, text="Check", padx=40, pady=20, command=check)
submit_button = tk.Button(root, text="Submit", padx=40, pady=20, command=submit)
repeat_button = tk.Button(root, text="Repeat", padx=40, pady=20, command=repeat)
done_BUTTON = tk.Button(root, text="Done", padx=40, pady=20, command=done)

check_value_button.grid(row=3, column=1)
submit_button.grid(row=3, column=3)
done_BUTTON.grid(row=3, column=2)
repeat_button.grid(row=3, column=1, columnspan=3)

root.mainloop()
