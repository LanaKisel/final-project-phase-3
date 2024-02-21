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
from pyfiglet import Figlet
f = Figlet(font='slant') 

def main():
    choice = 0
    print(f.renderText('___PRESCRIPTIONS MANAGER___'))
    print("Hello!\nWelcome to Prescriptions Manager!\nPlease use number keys to navigate.")
    while choice != 3:
        print('''
                What module would you like to enter?
                    1. - Patients
                    2. - Prescriptions
                    3. - Exit
        ''')

        choice = int(input())
        user_choice = 0
    
        if choice == 1:
            print("Entering Patient's Module...")
            while user_choice != 6:
                print('''
                Please choose an option:
                    1. - View Patients
                    2. - Find a patient by name 
                    3. - Add a patient
                    4. - Edit a patient
                    5. - Delete a patient 
                    6. - Go back to main menu
                    7. - Exit
                ''')

                user_choice = int(input())

                if user_choice == 1:                    
                    list_patients()

                if user_choice ==2:
                    find_patient_by_name()  

                if user_choice == 3:
                    create_patient()

                if user_choice == 4:
                    update_patient()

                if user_choice == 5:
                    delete_patient()

                if user_choice == 7:
                    exit_program()   

        if choice == 2:
            print("Entering Prescription's Module...")
            while user_choice != 7:
                print('''
                Please choose an option:
                    1. - View Prescriptions
                    2. - Find a prescription by medication name 
                    3. - Add a new prescription
                    4. - Edit a prescription
                    5. - Delete a prescription
                    6. - List patient's prescriptions
                    7. - Go back to main menu
                    8. - Exit
                ''')

                user_choice = int(input())

                if user_choice == 1:                    
                    list_prescriptions()

                if user_choice ==2:
                    find_prescription_by_name()  

                if user_choice == 3:
                    create_prescription()

                if user_choice == 4:
                    update_prescription()

                if user_choice == 5:
                    delete_prescription()

                if user_choice == 6:
                    list_patient_prescriptions()    

                if user_choice == 8:
                    exit_program()   

        if choice == 3:
            print("Exiting the Prescription Manager...")
            exit_program()

if __name__ == "__main__":
    main()
