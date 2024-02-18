# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    find_patient_by_id,
    find_patient_ny_name,
    create_patient,
    update_patient, delete_patient
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_patients()
        elif choice == "2":
            find_patient_by_id()
        elif choice == "3":
            find_patient_ny_name()
        elif choice == "4":
            create_patient()
        elif choice == "5":
            update_patient() 
        elif choice == "6":
            delete_patient()      
        else:
            print("Invalid choice")    


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all patients")
    print("2. Find patient by id")
    print("3. Find patient by name")
    print("4. Create new patient")
    print("5. Update patient")
    print("6. Delete patient")
    # print("")
    # print("")
    # print("")
    # print("")


if __name__ == "__main__":
    main()
