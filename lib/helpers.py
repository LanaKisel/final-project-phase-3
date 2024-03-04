# lib/helpers.py
from models.prescription import Prescription
from models.patient import Patient

def list_patients():
    patients = Patient.get_all()
    for index, patient in enumerate(patients):
        print(f"{index+1}. Patient 😷:{patient.name} {patient.surname}")
    return len(patients)

def find_patient():
    number_of_patients = list_patients()
    print("Enter number of the patient from the list above: ")
    patient_number = validate_choice(1, number_of_patients)
    patient = Patient.get_all()[patient_number-1]
    print(f"Patient 😷:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(
        f'Patient {name} not found')
    return patient.id    

def find_patient_by_name():
    name = validate_string_input("Enter patient's name: ", "Patient's name")
    patient = Patient.find_by_name(name)
    if patient:
        print(f"Patient 😷:\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}")
        return patient.id    
    else:
        print(f'Patient {name} not found')
        return None    

def create_patient():
    name = validate_string_input("Enter patient's name: ", "Patient's name")
    surname = validate_string_input("Enter patient's surname: ", "Patient's surname")
    address = validate_string_input("Enter patient's address: ", "Patient's address")
    try:
        patient = Patient.create(name, surname, address)
        print(f'Successfully added a new patient 😷\n\tPatient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient(id):
    if patient := Patient.find_by_id(id):
        try:
            name = validate_string_input("Enter patient's name: ", "Patient's name", patient.name)
            patient.name = name
            surname = validate_string_input("Enter patient's surname: ", "Patient's surname", patient.surname)
            patient.surname = surname
            address = validate_string_input("Enter patient's address: ", "Patient's address", patient.address)
            patient.address = address
            patient.update()
            print(f'Successfully updated patient 😷:\n\tMRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient not found') 

def delete_patient(id):
    if patient := Patient.find_by_id(id):
        patient.delete()
        print(f'Successfully deleted patient 😷\n\tMRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress:{patient.address}')
    else:
        print(f'Patient not found')

def list_prescriptions(patient_id= None):
    patient = Patient.find_by_id(patient_id)
    if patient_id:
        for index, prescription in enumerate(patient.prescriptions()):        
    # prescriptions = Prescription.get_all()
    # if not patient_id  == None:
    #     prescriptions = [prescription for prescription in prescriptions if prescription.patient_id == patient_id]
    # for index, prescription in enumerate(prescriptions):
        # patient = Patient.find_by_id(prescription.patient_id)
            print(f"{index +1}. Prescription💊:\n\tRX number: {prescription.rx_number}\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\t Refills: {prescription.refills}\nPatient😷: {patient.name} {patient.surname}\n\tPatient MRN: {patient.mrn}")
    if len(patient.prescriptions())==0:
        print("There are no prescriptions for this patient")
        return 0
    return len(patient.prescriptions())    

def  list_prescriptions_and_ask_for_prescription_input(patient_id= None):
    number_of_prescriptions = list_prescriptions(patient_id) 
    if number_of_prescriptions >0:
        print("Enter number of the prescription from the list above: ")
        prescription_number = validate_choice(1, number_of_prescriptions)
        if patient_id == None:
            prescription =  Prescription.get_all()[prescription_number-1]
        else:
            patient = Patient.find_by_id(patient_id)
            prescription = patient.prescriptions()[prescription_number-1]    
        # prescriptions = Prescription.get_all()
        # if not patient_id  == None:
        #     prescriptions = [prescription for prescription in prescriptions if prescription.patient_id == patient_id]
        # prescription = prescriptions[prescription_number-1]   
        print(f"Prescription💊:\n\tRX number: {prescription.rx_number}\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\t Refills: {prescription.refills}")
        return prescription.id    
    return None    

    
def find_prescription_by_name(id=None):
    number_of_prescriptions = list_prescriptions(id) 
    if number_of_prescriptions >0:
        medication = validate_string_input("Enter medication name: ", "Medication name")
        prescription = Prescription.find_by_name(medication)
        if prescription:
            print(f"Prescription:\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\t Refills: {prescription.refills}") 
            return prescription.id
        else:
            print(f'Prescription {medication} not found')  
    return None 

# def find_prescription_by_rx_number():
#     rx_number = validate_input("Enter prescription number: ", "rx_number", 1)
#     prescription = Prescription.find_by_rx_number(rx_number)
#     if prescription:
#         patient = Patient.find_by_id(prescription.patient_id)
#         print(f"Prescription:\n\tMedication name: {prescription.medication}.\n\tQty: {prescription.quantity}.\tRefills: {prescription.refills}.\nPatient:\n\tName: {patient.name}\tSurname: {patient.surname}\n\tPatient MRN: {patient.mrn}") 
#     else:
#         print(f'Prescription {rx_number} not found')        

def create_prescription(id):
    medication = validate_string_input("Enter medication name: ", "Medication name")
    quantity = validate_input("Enter medication quantity: ", "Quantity", 1)           
    refills = validate_input("Enter prescription's refills: ", 'Refills', 0)
    try:
        patient = Patient.find_by_id(id)
        if patient:
            prescription= Prescription.create(medication, quantity, refills, patient.id)
            print(f'Successfully created prescription.💊\n\tPatient 😷: {patient.name} {patient.surname}\n\tPrescription rx_number: {prescription.rx_number}.\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}')
        else:
            print(f"Patient not found ")             
    except Exception as exc:
        print("Error creating new prescription", exc)    

def update_prescription(id):
    if prescription := Prescription.find_by_id(id):
        try:
            patient = Patient.find_by_id(prescription.patient_id)         
            medication = validate_string_input(f"Enter medication name [{prescription.medication}]:  ", "Medication name", prescription.medication)
            prescription.medication = medication
            quantity = validate_input(f"Enter medication quantity [{prescription.quantity}]: ", "Quantity", 1, prescription.quantity)  
            prescription.quantity = quantity         
            refills = validate_input(f"Enter prescription's refills [{prescription.refills}]: ", 'Refills', 0, prescription.refills)
            prescription.refills = refills
            prescription.patient_id = patient.id
            prescription.update()
            print(f'Successfully updated prescription💊\n\tPrescription rx_number: {prescription.rx_number}.\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}\n\tPatient 😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}')
        except Exception as exc:
            print(f'Error updating prescription: ', exc) 
    else:
        print(f'Prescription not found')

def delete_prescription(id):
    if prescription := Prescription.find_by_id(id):
        patient = Patient.find_by_id(prescription.patient_id)
        prescription.delete()
        print(f'Successfully deleted prescription💊:\n\tRX number: {prescription.rx_number}\n\tMedication name:{prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}\n\tPatient😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}')
    else:
        print(f'Prescription not found')

# def list_patient_prescriptions(id):    
#     if patient := Patient.find_by_id(id):
#         for prescription in patient.prescriptions():
#             print(f"Prescription 💊:\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}")
#     else:
#         print(f'Patient not found')                    

def exit_program():
    print("Goodbye!👋")
    exit()

def validate_input(prompt, property_name, minimum_value, default_value=None):
    inpt= input(prompt)
    if inpt == '' and not default_value == None:
        inpt = default_value
        print(f'\t👉 Using {inpt} for {property_name}')
    if inpt == '' and default_value == None:
        print(f"{property_name} is required.")
        inpt = validate_input(prompt, property_name, minimum_value, default_value)    
    if type(inpt)== int and inpt < minimum_value:
        print(f"{inpt} is less than minimum required value for {property_name}. Please try again.")
        validate_input(prompt, property_name, minimum_value, default_value)
    return int(inpt)

def validate_string_input(prompt, property_name, default_value=None):
    inpt = input(prompt)
    if len(inpt) == 0 and not default_value == None:
        inpt = default_value
        print(f'\t👉 Using {inpt} for {property_name}')
    if len(inpt) == 0 and default_value == None:
        print(f"{property_name} is required.")
        inpt = validate_string_input(prompt, property_name, default_value)
    return inpt    

def validate_choice(min, max):
    input_text = input()
    while not input_text.isdigit() or int(input_text)<min or int(input_text)>max:
        print(f"Please enter the value between {min} and {max}")
        input_text = input()
    return int(input_text)


def find_patient_by_prescription_id(prescription_id):
    prescription = Prescription.find_by_id(prescription_id)
    patient_id = prescription.patient_id
    return patient_id
