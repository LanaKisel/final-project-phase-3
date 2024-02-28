# lib/helpers.py
from models.prescription import Prescription
from models.patient import Patient

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(f"Patient 😷:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name} \tSurname: {patient.surname}\n\tAddress: {patient.address}")

def find_patient_by_name():
    name = validate_string_input("Enter patient's name: ", "Patient's name")
    patient = Patient.find_by_name(name)
    print(f"Patient 😷:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(
        f'Patient {name} not found')

def find_patient_by_mrn():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number", 1)       
    patient = Patient.find_by_mrn(mrn_number)
    print(f"Patient 😷:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(        
    f'Patient {mrn_number} not found')

def create_patient():
    name = validate_string_input("Enter patient's name: ", "Patient's name")
    surname = validate_string_input("Enter patient's surname: ", "Patient's surname")
    address = validate_string_input("Enter patient's address: ", "Patient's address")
    try:
        patient = Patient.create(name, surname, address)
        print(f'Successfully added a new patient 😷\n\tPatient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    mrn_number = validate_input("Enter patient's medical record number: ", "medical record number", 1)
    if patient := Patient.find_by_mrn(mrn_number):
        try:
            name = validate_string_input("Enter patient's name: ", "Patient's name", patient.name)
            patient.name = name
            surname = validate_string_input("Enter patient's surname: ", "Patient's surname", patient.surname)
            patient.surname = surname
            address = validate_string_input("Enter patient's address: ", "Patient's address", patient.address)
            patient.address = address
            mrn = validate_input("Enter patinet's medical record number: ", "MRN", 1, patient.mrn)
            patient.mrn = mrn
            patient.update()
            print(f'Successfully updated patient 😷:\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress: {patient.address}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {mrn_number} not found') 

def delete_patient():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number", 1)
    if patient := Patient.find_by_mrn(mrn_number):
        patient.delete()
        print(f'Successfully deleted patient 😷\n\tMRN: {patient.mrn}\n\tName: {patient.name}\t Surname: {patient.surname}\n\tAddress:{patient.address}')
    else:
        print(f'Patient number {mrn_number} not found')

def list_prescriptions():
    prescriptions = Prescription.get_all()
    for prescription in prescriptions:
        patient = Patient.find_by_id(prescription.patient_id)
        print(f"Prescription💊:\n\tRX number: {prescription.rx_number}\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\t Refills: {prescription.refills}\nPatient😷:\n\tName: {patient.name}\t Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}")

def find_prescription_by_name():
    medication = validate_string_input("Enter medication name: ", "Medication name")
    prescription = Prescription.find_by_name(medication)
    if prescription:
        patient = Patient.find_by_id(prescription.patient_id)
        print(f"Prescription:\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\t Refills: {prescription.refills}\nPatient:\n\tName: {patient.name}\t Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}") 
    else:
        print(f'Prescription {medication} not found')

def find_prescription_by_rx_number():
    rx_number = validate_input("Enter prescription number: ", "rx_number", 1)
    prescription = Prescription.find_by_rx_number(rx_number)
    if prescription:
        patient = Patient.find_by_id(prescription.patient_id)
        print(f"Prescription:\n\tMedication name: {prescription.medication}.\n\tQty: {prescription.quantity}.\tRefills: {prescription.refills}.\nPatient:\n\tName: {patient.name}\tSurname: {patient.surname}\n\tPatient MRN: {patient.mrn}") 
    else:
        print(f'Prescription {rx_number} not found')        

def create_prescription():
    medication = validate_string_input("Enter medication name: ", "Medication name")
    quantity = validate_input("Enter medication quantity: ", "Quantity", 1)           
    refills = validate_input("Enter prescription's refills: ", 'Refills', 0)
    mrn = validate_input("Enter patient's mrn:  ", "Patient's MRN", 1)
    try:
        patient = Patient.find_by_mrn(mrn)
        if patient:
            prescription= Prescription.create(medication, quantity, refills, patient.id)
            print(f'Successfully created prescription.💊\n\tPrecription rx_number: {prescription.rx_number}.\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}\n\tPatient 😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}')
        else:
            print(f"Patient with MRN: {mrn} is not found ")             
    except Exception as exc:
        print("Error creating new prescription", exc)    

def update_prescription():
    rx_number = validate_input("Enter prescription number: ", "RX_number", 1)
    if prescription := Prescription.find_by_rx_number(rx_number):
        try:
            patient = Patient.find_by_id(prescription.patient_id)         
            medication = validate_string_input("Enter medication name: ", "Medication name", prescription.medication)
            prescription.medication = medication
            quantity = validate_input("Enter medication quantity: ", "Quantity", 1, prescription.quantity)  
            prescription.quantity = quantity         
            refills = validate_input("Enter prescription's refills: ", 'Refills', 0, prescription.refills)
            prescription.refills = refills
            mrn = validate_input("Enter patient's mrn:  ", "Patient's MRN", 1, patient.mrn)
            patient = Patient.find_by_mrn(mrn)
            prescription.patient_id = patient.id
            prescription.update()
            print(f'Successfully updated prescription💊\n\tPrecription rx_number: {prescription.rx_number}.\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}\n\tPatient 😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}')
        except Exception as exc:
            print(f'Error updating prescription: ', exc) 
    else:
        print(f'Prescription {rx_number} not found')

def delete_prescription():
    rx_number = validate_input("Enter prescription  number: ", "RX_number", 1)
    if prescription := Prescription.find_by_rx_number(rx_number):
        patient = Patient.find_by_id(prescription.patient_id)
        prescription.delete()
        print(f'Successfully deleted prescription💊:\n\tRX number: {prescription.rx_number}\n\tMedication name:{prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}\n\tPatient😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}')
    else:
        print(f'Prescription {rx_number} not found')

def list_patient_prescriptions():
    mrn_number = validate_input("Enter patient's medical record number: ", "Patient MRN", 1)
    if patient := Patient.find_by_mrn(mrn_number):
        print(f"Patient 😷:\n\tName: {patient.name} Surname: {patient.surname}\n\tPatient MRN: {patient.mrn}")
        for prescription in patient.prescriptions():
            print(f"Prescription 💊:\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\tRefills: {prescription.refills}")
    else:
        print(f'Patient {mrn_number} not found')                    

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