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
    find_prescription_by_rx_number,
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
        operation_choice = 0
        patient_operations_choice = 0
        rx_operation_choice = 0
        patient_prescription_operation_choice=0
        named_prescription_operation_choice = 0

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


                        if operation_choice == 3:
                            exit()
     
                   

                if user_choice == 2:
                    find_patient_by_name()
                if user_choice == 3:
                    create_patient()
                if user_choice == 5:
                    exit()                
    


# def main():
#     choice = 0
#     print(f.renderText('___PRESCRIPTIONS MANAGER___'))
#     print("Hello!\nWelcome to Prescriptions Manager!\nPlease use number keys to navigate.")
    # while choice != 3:
    #     print('''
    #             What module would you like to enter?
    #                 1. - Patients
    #                 2. - Prescriptions
    #                 3. - Exit
    #     ''')
         
#         choice = int(input())
#         user_choice = 0

        # if choice == 1:
        #     print("Entering Patient's Module...")
        #     while user_choice != 7:
        #         print('''
        #         Please choose an option:
        #             1. - View Patients
        #             2. - Find a patient by name
        #             3. - Look up patient
        #             4. - Add a new patient
        #             5. - Edit patient
        #             6. - Delete a patient 
        #             7. - Go back to main menu
        #             8. - Exit
        #         ''')

        #         user_choice = int(input())

#                 if user_choice == 1:                    
#                     list_patients()

#                 if user_choice ==2:
#                     find_patient_by_name()

#                 if user_choice ==3:
#                     find_patient()      

#                 if user_choice == 4:
#                     create_patient()

#                 if user_choice == 5:
#                     update_patient()

#                 if user_choice == 6:
#                     delete_patient()

#                 if user_choice == 8:
#                     exit_program()   

#         if choice == 2:
#             print("Entering Prescription's Module...")
#             while user_choice != 7:
#                 print('''
#                 Please choose an option:
#                     1. - View Prescriptions
#                     2. - Find a prescription by medication name 
#                     3. - Add a new prescription
#                     4. - Edit a prescription
#                     5. - Delete a prescription
#                     6. - List patient's prescriptions
#                     7. - Go back to main menu
#                     8. - Exit
#                 ''')

#                 user_choice = int(input())

#                 if user_choice == 1:                    
#                     list_prescriptions()

#                 if user_choice ==2:
#                     find_prescription_by_name()  

#                 if user_choice == 3:
#                     create_prescription()

#                 if user_choice == 4:
#                     update_prescription()

#                 if user_choice == 5:
#                     delete_prescription()

#                 if user_choice == 6:
#                     list_patient_prescriptions()    

#                 if user_choice == 8:
#                     exit_program()   

#         if choice == 3:
#             print("Exiting the Prescription Manager...")
#             exit_program()

if __name__ == "__main__":
    main()
