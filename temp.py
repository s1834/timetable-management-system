import csv
import random
import time



#__main__
def main():
    print("\nTimetable Management System For School\n")
    time.sleep(2)

    # Ask the users whether they want to create or read a timetable
    user = 1
    user = user_type()

    # Verify user id and password for writing operations
    if user == 0:
        verification = 1
        incorrect = 1
        while verification == 1:
            verification = user_verification(0)
            if verification == 0:
                # Generate timetables with the help of multiple functions
                generate_timetable()
            elif incorrect >= 2 and incorrect <= 4:
                incorrect = incorrect + 1
                forgot = 2
                while not forgot == 0  and not forgot == 1:
                    forgot = int(input("Did you forgot your username or password?\n To Change your password, Enter 0\n To retry, Enter 1\n Your Choice: "))
                    if not forgot == 0 and not forgot == 1:
                        print("You can only choose 0 or 1")
                    elif forgot == 0:
                        verification = user_verification(1)
                    else:
                        verification = user_verification(0)
            elif incorrect >= 5:
                print("Wrong Username or Password Entered Multiple Times!!!")
                print("Access Denied!!!")
                time.sleep(2)
                return 1
            else:
                print("Username or Password Incorrect\n")
                incorrect = incorrect + 1
    
    # Read timetables using access code
    else:
        view()



# Ask the users whether they want to create or read a timetable
def user_type():
    user = 2
    while not user == 0 and not user == 1:
        user = int(input("What do you want to do?\n To create a timetable, Enter 0\n To view already created timetable, Enter 1\n Your Choice: "))
    return user



# Verify user id and password for writing operations
def user_verification(verify):
    user_id = "temp"
    password = "temp"
    root_password = "pmet"
    if verify == 0:
        print()
        user_id_temp = input("User Id: ")
        password_temp = input("Password: ")

        if user_id == user_id_temp and password == password_temp:
            return 0
        else:
            return 1
    
    # Create a temprory password for login
    else:
        user_id_temp = input("User Id: ")
        if user_id == user_id_temp:
            root_password_temp = input("Root Password: ")
            if root_password == root_password_temp:
                password = input("Enter Temporary access password")
            else:
                print("Incorrect Root Password!!!")
                print("Access Denied!!!")
                time.sleep(2)
                return 1



# Generate timetables with the help of multiple functions
def generate_timetable():

    # Get number of subjects
    no_of_subjects = 0
    while no_of_subjects <= 0 or no_of_subjects >= 10:
        print("\nNOTE: Number of Subjects = Number of Teachers = Number of Classes = Number of Periods")
        time.sleep(1)
        no_of_subjects = int(input("Enter Number Of Subjects: "))
        if no_of_subjects == 0 or no_of_subjects >= 10:
            print("Number Of Subjects should be more than 0 and less than 10\n")
    print()

    # Get name of subjects
    name_of_subjects = get_subject_names(no_of_subjects)
    name_of_class = get_class_names(no_of_subjects)
    if name_of_subjects == 1:
        return 1

    #get number of periods
    no_of_periods = get_periods(no_of_subjects)

    # Days column in CSV file
    timetable_Days = [["Day↓/Period→"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"], ["Friday"], ["Saturday"]]
    # Periods row and periods for each day in CSV file
    timetable_Periods = [no_of_periods, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects]
    print()

    # Get the choice for customized timetable
    choice = 2
    while not choice == 0 and not choice == 1:
        choice = int(input("Choose how do you want your timetable?\n Press 0 for same timetable everyday\n Press 1 for random timetable everyday\n Your Choice: "))
        if not choice == 0 and not choice == 1:
            print("You can only choose 0 or 1\n")
    print()

    # Creates a CSV file for timetable with same periods everyday
    if choice == 0:
        create_same_timetable_file(timetable_Days, timetable_Periods, name_of_class)
        print("\nYour timetable is saved in a file with prefix timetable_same_\n")
    
    # Creates a CSV file for timetable with random periods everyday
    if choice == 1:
        create_random_timetable_file(timetable_Days, timetable_Periods, name_of_subjects)
        print("\nYour timetable is saved in a file with prefix timetable_random_\n")
    return 0



# Get name of subjects
def get_subject_names(no_of_subjects):
    subjects_list = []
    print("Enter Name Of Subjects and Teachers {FORMAT: Subject(Name of Teacher)}")
    time.sleep(1)
    for number in range(no_of_subjects):
        subject = input("Enter Name Of Subject and Teacher " + str(number + 1) + ": ")
        subject = subject.capitalize()
        if not subject in subjects_list:
            subjects_list.append(subject)
        else:
            print(subject + " Already Exists")
            return 1
    return subjects_list



# Get name of classes
def get_class_names(no_of_subjects):
    classes_list = []
    print("\nEnter Name of Class in English Language (i.e. Twelfth, Eleventh, etc.)")
    time.sleep(1)
    for number in range(no_of_subjects):
        classes = input("Enter Name of Class " + str(number + 1) + ": ")
        classes = classes.capitalize()
        if not classes in classes_list:
            classes_list.append(classes)
        else:
            print(classes + " Already Exists")
            return 1
    return classes_list



# Get number of period
def get_periods(no_of_subjects):
    periods_list = []
    for number in range(no_of_subjects):
        periods_list.append(number + 1)
    return periods_list



# Creates CSV files for timetable with same periods everyday
def create_same_timetable_file(timetable_Days, timetable_Periods, name_of_class):
    for classes in range (len(name_of_class)):
        file_name = "timetable_same_" + name_of_class[classes] + ".csv"
        with open(file_name, "w") as timetables:
            print("\nTimetable for Class " + name_of_class[classes].capitalize())
            timetables_writer = csv.writer(timetables)

            # Does main writing and printing of timetable
            for row in range(7):
                # Concatenates respective rows and columns
                timetable = timetable_Days[row] + timetable_Periods[row]
                # Writes one row at a time in CSV file
                timetables_writer.writerow(timetable)
                # Prints timetable row after row (i.e. day after day) on OUTPUT screen
                print(timetable)
        print("Your timetable is saved in a file called " + file_name)
    return 0



# Creates a CSV file for timetable with random periods everyday
def create_random_timetable_file(timetable_Days, timetable_Periods, name_of_subjects, name_of_class):
    for classes in range (len(name_of_class)):
        file_name = "timetable_random_" + name_of_class[classes] + ".csv"
        with open(file_name, "w") as timetables:
            timetables_writer = csv.writer(timetables)

            # Does main writing and printing of timetable
            for row in range(7):
                random.shuffle(name_of_subjects)
                # Concatenates respective rows and columns
                timetable = timetable_Days[row] + timetable_Periods[row]
                # Writes one row at a time in CSV file
                timetables_writer.writerow(timetable)
                # Prints timetable row  after row (i.e. day after day) on OUTPUT screen
                print(timetable)
        print("Your timetable is saved in a file called " + file_name)
    return 0



# Read timetables using access code
def view():
    access_code = 1
    incorrect_code = 0
    while access_code == 1:
        access_code = get_access_code()
        if access_code == 0:
            choice = 2
            while not choice == 0 and not choice == 1:
                choice = int(input("Choose which timetable you want to see?\n Press 0 for same timetable everyday\n Press 1 for random timetable everyday\n Your Choice: "))
                if not choice == 0 and not choice == 1:
                    print("You can only choose 0 or 1\n")
            print()

            # Reads CSV files for timetable with same periods everyday
            if choice == 0:
                read_same_timetable_file()

            # Reads CSV files for timetable with random periods everyday
            if choice == 1:
                read_random_timetable_file()
            return 0

        elif incorrect_code == 3:
            print("Access Denied!")
            return 1
        else:
            print("Incorrect Code")
            incorrect_code = incorrect_code + 1
    return 0



# Reads CSV files for timetable with same periods everyday
def read_same_timetable_file():
    with open("timetable_same.csv", "r") as timetables:
        timetables_reader = csv.reader(timetables)
        for rows in timetables_reader:
            print(rows)



# Reads CSV files for timetable with random periods everyday
def read_random_timetable_file():
    with open("timetable_random.csv", "r") as timetables:
        timetables_reader = csv.reader(timetables)
        for rows in timetables_reader:
            print(rows)



# Gets and Verifies access code for reading functions
def get_access_code():
    access_code = "1234"
    access_code_temp = input("Enter Access Code: ")
    if access_code == access_code_temp:
        return 0
    else:
        return 1



# Executes __main__ function
main()