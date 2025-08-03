from datetime import *
from pandas import *
from smtplib import *
from random import *
from tkinter import *
from tkinter import messagebox

EMAIL = "derinazrairem@gmail.com"
PASSWORD = "gujumnpflgpiegjr"

# ------------------------------------- SAVE -------------------------------------- #
def save():
    name_get = name_entry.get()
    mail_get = mail_entry.get()

    try:
        year_get = int(year_entry.get())
        day_get = int(day_entry.get())
        month_get = int(month_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric values for year, month and day.")
        return

    if not (name_get and mail_get and year_get and month_get and day_get):
        messagebox.showinfo(title="Oops", message="Please dont' leave any fields empty.")
        return
    else:
        is_ok = messagebox.askokcancel(
            title="Confirm Info",
            message=f"These are the details entered:\n"
                    f"Name: {name_get}\nEmail: {mail_get}\n"
                    f"Year: {year_get}, Month: {month_get}, Day: {day_get}\n"
                    f"Is it okay to save?")
    if is_ok:
        with open("birthdays.csv", "a") as data:
            data.write(f"{name_get},{mail_get},{year_get},{month_get},{day_get}\n")

    name_entry.delete(0, END)
    mail_entry.delete(0, END)
    year_entry.delete(0, END)
    month_entry.delete(0, END)
    day_entry.delete(0, END)

    messagebox.showinfo("Saved", "Birthday has been saved successfully!")

# -------------------------------------- CSV -------------------------------------- #
def check_and_send():
    now = datetime.now()
    month = now.month
    day=now.day

    file = read_csv("birthdays.csv")
    file_dict = file.to_dict(orient="records")

    for birthday in file_dict:
        if birthday["month"] == month and birthday["day"] == day:
            name = birthday["name"]
            email = birthday["email"]

            letter_num = choice([1, 2, 3])
            with open(f"letter_templates/letter_{letter_num}.txt", "r") as file:
                letter_content = file.read()

            final_letter = letter_content.replace("[NAME]", name)

            with SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:HAPPY BIRTHDAY!\n\n{final_letter}")

                messagebox.showinfo("Email Sent", f"Birthday email sent to {name}!")

            for person in file_dict:
                if person["email"] != email:
                    with open(f"letter_templates/letter_reminder.txt", "r") as file:
                        reminder_content = file.read()

                    reminder = reminder_content.replace("[Name]", person["name"]).replace("X", name)

                    with SMTP("smtp.gmail.com", port=587) as connection:
                        connection.starttls()
                        connection.login(user=EMAIL, password=PASSWORD)
                        connection.sendmail(from_addr=EMAIL,
                                            to_addrs=person["email"],
                                            msg=f"Subject:Reminder:\n\n{reminder}")
# -------------------------------------- GUI -------------------------------------- #
window = Tk()
window.title("Birthday Saver")
window.config(padx=50, pady=50)

name_text = Label(text="Name:")
name_text.grid(row=0, column=0)

mail_text = Label(text="Email:")
mail_text.grid(row=1, column=0)

year_text = Label(text="Year:")
year_text.grid(row=2, column=0)

day_text = Label(text="Day (1-31):")
day_text.grid(row=3, column=0)

month_text = Label(text="Month (1-12):")
month_text.grid(row=4, column=0)

name_entry = Entry()
name_entry.grid(row=0, column=1)

mail_entry = Entry()
mail_entry.grid(row=1, column=1)

year_entry = Entry()
year_entry.grid(row=2, column=1)

day_entry = Entry()
day_entry.grid(row=3, column=1)

month_entry = Entry()
month_entry.grid(row=4, column=1)

save_button = Button(text="Save", command=save)
save_button.grid(row=5, column=1, columnspan=2, sticky="ew")

send_button = Button(text="Send Today's Wishes", command=check_and_send)
send_button.grid(row=6, column=1, columnspan=2, sticky="ew")
window.mainloop()
