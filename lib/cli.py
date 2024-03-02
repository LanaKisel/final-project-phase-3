# lib/cli.py

from helpers import (
    exit_program,
    list_patients,
    #find_patient_by_mrn,
    find_patient_by_name,
    find_patient,
    create_patient,
    update_patient, delete_patient,
    list_prescriptions,
    find_prescription,
    #find_prescription_by_rx_number,
    find_prescription_by_name,
    create_prescription,
    update_prescription,
    delete_prescription,
    list_patient_prescriptions,
    find_patient_by_prescription_id
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
        prescription_choice = 0
        operation_choice = 0
        prescription_choice = 0
        prescription_operation_choice = 0

        if choice  == 1:
            print("Entering Patient's Module...")
            user_choice = 0
            while user_choice != 5:
                print('''
                Please choose an option:
                    1. - View Patients
                    2. - Look up a patient by name
                    3. - Add a new patient
                    4. - Go back to main menu
                    5. - Exit
                ''')

                user_choice = int(input())

                if user_choice == 1:
                    list_patients()
                    print("What would you like to do next?") 
                    operation_choice = 0
                    while operation_choice !=2:
                        print('''
                            Please choose an option:
                                1. - Choose a patient
                                2. - Return to Patient module manu
                                3. - Exit
                        ''')
                        operation_choice = int(input())
                        if operation_choice ==1:                           
                            patient_id = find_patient()
                            patient_prescription_menu(patient_id)   


                        if operation_choice == 3:
                            exit()   
                if user_choice == 2:
                    patient_id = find_patient_by_name()
                    if patient_id == None:
                        continue
                    patient_prescription_menu(patient_id)                        

                if user_choice == 3:
                    create_patient()
                if user_choice == 5:
                    exit() 

        if choice ==2:
            print("Entering Prescription's Module...")
            prescription_choice = 0
            while prescription_choice != 2:
                print('''
                Please choose an option:
                    1. - View all prescriptions
                    2. - Go back to main menu
                    3. - Exit
                ''')

                prescription_choice = int(input())
                if prescription_choice ==1:
                    list_prescriptions()
                    print("What would you like to do next?")
                    prescription_operation = 0
                    while prescription_operation !=2:
                        print('''
                            Please choose your option:
                                1. - Choose prescription
                                2. - Previous menu
                                3. - Exit
                        ''')
                        prescription_operation = int(input())

                        if prescription_operation == 1:
                            prescription_id = find_prescription()
                            patient_id = find_patient_by_prescription_id(prescription_id)
                            prescription_operation_choice = 0
                            while prescription_operation_choice !=4:                                
                                print('''
                                    Please choose your option:
                                        1. - Patient's information
                                        2. - Edit prescription
                                        3. - Delete prescription
                                        4. - Previous menu
                                        5. - Exit
                                ''')
                                prescription_operation_choice = int(input())
                                if prescription_operation_choice == 1:
                                    patient_prescription_menu(patient_id)
                                if prescription_operation_choice == 2:
                                    update_prescription(prescription_id)
                                if prescription_operation_choice == 3:
                                    delete_prescription(prescription_id)
                                if prescription_operation_choice == 5:
                                    exit()   
                        if prescription_operation ==3:
                            exit()    
                if prescription_choice ==3:
                    exit()
    
def patient_prescription_menu(patient_id):
    print("What would you like to do next?")
    patient_operations_choice = 0
    while patient_operations_choice !=4:
        print('''
            Please choose an option:
                1. - Edit patinet's personal information
                2. - Patient's prescriptions
                3. - Delete a patient
                4. - Return to previous menu
                5. - Exit
        ''') 

        patient_operations_choice = int(input())
        
        if patient_operations_choice == 1:
            update_patient(patient_id)
        if patient_operations_choice == 2:    
            patient_prescription_operation_choice = 0
            while patient_prescription_operation_choice !=4:                                
                print('''
                    What would you like to do next?
                        1. - View All prescriptions
                        2. - Find prescription by medication
                        3. - Add a prescription
                        4. - Return to previous menu
                        5. - Exit   
                ''')
                patient_prescription_operation_choice = int(input())

                if patient_prescription_operation_choice == 1:                                        
                    prescription_id = find_prescription(patient_id)
                    if prescription_id == None:
                        continue
                    print("What would you like to do next?")    
                    rx_operation_choice = 0
                    while rx_operation_choice != 3:
                        print('''
                            Please choose an option:
                                1. - Edit prescription
                                2. - Delete a prescription
                                3. - Return to previous menu
                                4. - Exit
                            ''')                                        
                        rx_operation_choice = int(input())

                        if rx_operation_choice == 1:
                            update_prescription(prescription_id)
                        if rx_operation_choice ==2:
                            delete_prescription(prescription_id)
                        if rx_operation_choice ==4:
                            exit()        
                    
                if patient_prescription_operation_choice ==2:
                    prescription_id = find_prescription_by_name(patient_id)
                    if prescription_id == None:
                        continue
                    print("What would you like to do next?")    
                    named_prescription_operation_choice = 0
                    while named_prescription_operation_choice != 3:
                        print('''
                            Please choose an option:
                                1. - Edit prescription
                                2. - Delete a prescription
                                3. - Return to previous menu
                                4. - Exit
                            ''')
                        named_prescription_operation_choice = int(input())

                        if named_prescription_operation_choice ==1:
                            update_prescription(prescription_id)
                        if named_prescription_operation_choice ==2:
                            delete_prescription(prescription_id)
                        if named_prescription_operation_choice ==4:
                            exit()
                            
                if patient_prescription_operation_choice ==3:
                    create_prescription(patient_id)
                if patient_prescription_operation_choice == 5:
                    exit()                    
            
        if patient_operations_choice == 3:
            delete_patient(patient_id)    
        if patient_operations_choice == 5:
            exit() 

    # if choice ==2:
    #     print("Entering Prescription's Module...")
    #     prescription_choice = 0
    #     while prescription_choice != 2:
    #         print('''
    #         Please choose an option:
    #             1. - View all prescriptions
    #             2. - Go back to main menu
    #             3. - Exit
    #         ''')

    #         prescription_choice = int(input())
    #         if prescription_choice ==1:
    #             list_prescriptions()
    #             print("What would you like to do next?")
    #             prescription_operation = 0
    #             while prescription_operation !=2:
    #                 print('''
    #                     Please choose your option:
    #                         1. - Choose prescription
    #                         2. - Previous menu
    #                         3. - Exit
    #                 ''')
    #                 prescription_operation = int(input())

    #                 if prescription_operation == 1:
    #                     prescription_id = find_prescription()
    #                     display_patient_by_prescription_id(prescription_id)
    #                     prescription_operation_choice = 0
    #                     while prescription_operation_choice !=4:                                
    #                         print('''
    #                             Please choose your option:
    #                                 1. - Patient's information
    #                                 2. - Edit prescription
    #                                 3. - Delete prescription
    #                                 4. - Previous menu
    #                                 5. - Exit
    #                         ''')
    #                         prescription_operation_choice = int(input())
    #                         if prescription_operation_choice == 1:
    #                             patient_prescription_menu(patient_id)
    #                         if prescription_operation_choice == 2:
    #                             update_prescription(prescription_id)
    #                         if prescription_operation_choice == 3:
    #                             delete_prescription(prescription_id)
    #                         if prescription_operation_choice == 5:
    #                             exit()   
    #                 if prescription_operation ==3:
    #                     exit()    
    #         if prescription_choice ==3:
    #             exit()

if __name__ == "__main__":
    main()
