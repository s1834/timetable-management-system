import csv
import random

#__main__
def main():
    print("\nTimetable Management System For School\n")
    # Get number of subjects
    no_of_subjects = 0
    while no_of_subjects <= 0 or no_of_subjects >= 10:
        no_of_subjects = int(input("Enter Number Of Subjects: "))
        if no_of_subjects == 0 or no_of_subjects >= 10:
            print("Number Of Subjects should be more than 0 and less than 10\n")
    print()
    # Get name of subjects
    name_of_subjects = get_subject_names(no_of_subjects)
    if name_of_subjects == 1:
        return 1
    #get number of periods
    no_of_periods = get_periods(no_of_subjects)
    # Days column in CSV file
    timetable_Days = [["Day↓/Period→"], ["Monday"], ["Tuesday"], ["Wednesday"], ["Thursday"], ["Friday"], ["Saturday"]]
    # Periods row and periods for each day in CSV file
    timetable_Periods = [no_of_periods, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects, name_of_subjects]
    print()
    choice = 2
    while not choice == 0 and not choice == 1:
        choice = int(input("Choose do you want your timetable?\n Press 0 for same timetable everyday\n Press 1 for random timetable everyday\n Your Choice: "))
        if not choice == 0 and not choice == 1:
            print("You can only choose 0 or 1\n")
    print()
    # Creates a CSV file for timetable with same periods everyday
    if choice == 0:
        create_same_timetable_file(timetable_Days, timetable_Periods)
        print("\nYour timetable is saved in a file called timetable_same.csv\n")
    # Creates a CSV file for timetable with random periods everyday
    if choice == 1:
        create_random_timetable_file(timetable_Days, timetable_Periods, name_of_subjects)
        print("\nYour timetable is saved in a file called timetable_random.csv\n")
    return 0

# Get name of subjects
def get_subject_names(no_of_subjects):
    subjects_list = []
    for number in range(no_of_subjects):
        subject = input("Enter Name Of Subject " + str(number + 1) + ": ")
        subject = subject.capitalize()
        if not subject in subjects_list:
            subjects_list.append(subject)
        else:
            print(subject + " Already Exists")
            return 1
    return subjects_list

# Get number of periods
def get_periods(no_of_subjects):
    periods_list = []
    for number in range(no_of_subjects):
        periods_list.append(number + 1)
    return periods_list

# Creates a CSV file for timetable with same periods everyday
def create_same_timetable_file(timetable_Days, timetable_Periods):
    with open("timetable_same.csv", "w") as timetables:
        timetables_writer = csv.writer(timetables)
        # Does main writing and printing of timtable
        for row in range(7):
            # Concatenates respective rows and columns
            timetable = timetable_Days[row] + timetable_Periods[row]
            # Writes one row at a time in CSV file
            timetables_writer.writerow(timetable)
            # Prints timetable row after row (i.e. day after day) on OUTPUT screen
            print(timetable)
    return 0

# Creates a CSV file for timetable with random periods everyday
def create_random_timetable_file(timetable_Days, timetable_Periods, name_of_subjects):
    with open("timetable_random.csv", "w") as timetables:
        timetables_writer = csv.writer(timetables)
        # Does main writing and printing of timetable
        for row in range(7):
            random.shuffle(name_of_subjects)
            # Conccatenates respective rows and columns
            timetable = timetable_Days[row] + timetable_Periods[row]
            # Writes one row at a time in CSV file
            timetables_writer.writerow(timetable)
            # Prints timetable row  after row (i.e. day after day) on OUTPUT screen
            print(timetable)
    return 0

# Executes __main__ function
main()