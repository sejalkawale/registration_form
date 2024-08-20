import tkinter as tk
from tkinter import ttk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Form")

        self.main_frame = tk.Frame(self.root, bg="gray")
        self.main_frame.pack(fill="both", expand=True)

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.contact_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.main_frame, text="Name", bg="gray").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Email", bg="gray").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.email_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Age", bg="gray").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.age_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Contact No", bg="gray").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.contact_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Gender", bg="gray").grid(row=4, column=0, padx=5, pady=5)
        gender_frame = tk.Frame(self.main_frame, bg="gray")
        male_radio = tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male")
        female_radio = tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female")
        male_radio.pack(side="left")
        female_radio.pack(side="left")
        gender_frame.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Password", bg="gray").grid(row=6, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.password_var, width=30, show="*").grid(row=6, column=1, padx=5, pady=5)

        tk.Label(self.main_frame, text="Confirm Password", bg="gray").grid(row=7, column=0, padx=5, pady=5)
        tk.Entry(self.main_frame, textvariable=self.confirm_password_var, width=30, show="*").grid(row=7, column=1, padx=5, pady=5)

        submit_button = tk.Button(self.main_frame, text="Submit", command=self.submit_fields)
        submit_button.grid(row=8, column=1, padx=5, pady=5)

    def submit_fields(self):
        name = self.name_var.get()
        email = self.email_var.get()
        age = self.age_var.get()
        contact = self.contact_var.get()
        gender = self.gender_var.get()
        password = self.password_var.get()
        confirm_password = self.confirm_password_var.get()

        if password != confirm_password:
            print("Passwords do not match")
        else:
            print("Name: ", name)
            print("Email: ", email)
            print("Age: ", age)
            print("Contact No: ", contact)
            print("Gender: ", gender)
            print("Password: ", password)

root = tk.Tk()
app = RegistrationForm(root)
root.mainloop()