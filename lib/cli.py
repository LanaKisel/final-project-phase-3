# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    find_patient_by_id,
    find_patient_by_name,
    create_patient,
    update_patient, delete_patient,
    list_prescriptions,
    find_prescription_by_id,
    find_prescription_by_name,
    create_prescription,
    update_prescription,
    delete_prescription,
    list_patient_prescriptions
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
            find_patient_by_name()
        elif choice == "4":
            create_patient()
        elif choice == "5":
            update_patient() 
        elif choice == "6":
            delete_patient()
        elif choice == "7":
            list_prescriptions()
        elif choice == "8":
            find_prescription_by_id()
        elif choice == "9":
            find_prescription_by_name()
        elif choice == "10":
            create_prescription()
        elif choice == "11":
            update_prescription()
        elif choice == "12":
            delete_prescription()
        elif choice == "13":
            list_patient_prescriptions()                                  
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
    print("7. List all prescriptions")
    print("8. Find prescription by id")
    print("9. Find prescription by medication name")
    print("10. Create new prescription")
    print("11. Update prescription")
    print("12. Delete prescription")
    print("13. List all patient's prescriptions")


if __name__ == "__main__":
    main()
