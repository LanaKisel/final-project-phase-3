# lib/helpers.py
from models.prescription import Prescription
from models.patient import Patient

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(f"Patient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}")

def find_patient_by_name():
    name = input("Enter patient's name: ")
    patient = Patient.find_by_name(name)
    print(f"Patient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(
        f'Patient {name} not found')

# def find_patient_by_id():
#     mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")       
#     patient = Patient.find_by_id(mrn_number)
#     print(f"Patient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(        
#     f'Patient {mrn_number} not found')

def find_patient_by_mrn():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")       
    patient = Patient.find_by_mrn(mrn_number)
    print(f"Patient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}") if patient else print(        
    f'Patient {mrn_number} not found')


def create_patient():
    name = input("Enter patient's name: ")
    surname = input("Enter patient's surname: ")
    address = input("Enter patient's address: ")
    mrn = int(input("Enter patient's medical record number: "))
    try:
        patient = Patient.create(name, surname, address, mrn)
        print(f'Successfully added a new patient.\n\tPatient:\n\tPatient MRN: {patient.mrn}\n\tName: {patient.name}\n\tSurname: {patient.surname}\n\tAddress: {patient.address}"')
    except Exception as exc:
        print("Error creating patient: ", exc)

# def update_patient():
#     mrn_number = validate_input("Enter patient's medical record number: ", "medical record number")
#     if patient := Patient.find_by_id(mrn_number):
#         try:
#             name = input("Enter patient's name: ")
#             if len(name) == 0:
#                 name = patient.name
#             patient.name = name
#             surname = input("Enter patient's surname: ")
#             if len(surname) == 0:
#                 surname = patient.surname
#             patient.surname = surname
#             address = input("Enter patient's address: ")
#             if len(address) == 0:
#                 address = patient.address
#             patient.address = address
#             patient.update()
#             print(f'Success: {patient}')
#         except Exception as exc:
#             print("Error updating patient: ", exc)
#     else:
#         print(f'Patient {mrn_number} not found')    

def update_patient():
    mrn_number = validate_input("Enter patient's medical record number: ", "medical record number")
    if patient := Patient.find_by_mrn(mrn_number):
        try:
            name = input("Enter patient's name: ")
            if len(name) == 0:
                name = patient.name
            patient.name = name
            surname = input("Enter patient's surname: ")
            if len(surname) == 0:
                surname = patient.surname
            patient.surname = surname
            address = input("Enter patient's address: ")
            if len(address) == 0:
                address = patient.address
            patient.address = address
            mrn = input("Enter patient's MRN: ")
            if len(mrn) == 0:
                mrn = patient.mrn
            patient.mrn = mrn
            patient.update()
            print(f'Success: {patient}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {mrn_number} not found') 

# def delete_patient():
#     mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")
#     if patient := Patient.find_by_id(mrn_number):
#         patient.delete()
#         print(f'Success {mrn_number} deleted')
#     else:
#         print(f'Patient {mrn_number} not found')

def delete_patient():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")
    if patient := Patient.find_by_mrn(mrn_number):
        patient.delete()
        print(f'Success {mrn_number} deleted')
    else:
        print(f'Patient {mrn_number} not found')

def list_prescriptions():
    prescriptions = Prescription.get_all()
    for prescription in prescriptions:
        patient = Patient.find_by_id(prescription.patient_id)
        print(f"Prescription:\n\tMedication name: {prescription.medication}.\n\tQty: {prescription.quantity}.\tRefills: {prescription.refills}.\n\tPatient's name: {patient.name}.")

def find_prescription_by_name():
    medication = input("Enter medication name: ")
    prescription = Prescription.find_by_name(medication)
    print(prescription) if prescription else print(
        f'Prescription {medication} not found')

def find_prescription_by_id():
    rx_number = validate_input("Enter prescription number: ", "rx_number")
    prescription = Prescription.find_by_id(rx_number)
    print(prescription) if prescription else print(
        f'Prescription {rx_number} not found')

def create_prescription():
    medication = input("Enter medication name: ")
    quantity = int(input("Enter quantity of medication: "))
    refills = int(input("Enter presciption's refills: "))
    patient_mrn = int(input("Enter patient_mrn: "))
    try:
        patient = Patient.find_by_mrn(patient_mrn)
        if patient:
            prescription= Prescription.create(medication, quantity, refills, patient.id)
            print(f'Successfully created prescription.\n\t Precription rx_number: {prescription.rx_number}.\n\tMedication name: {prescription.medication}\n\tQty: {prescription.quantity}\n\tRefills: {prescription.refills}\n\tPatient\'s name: {patient.name}.')
        else:
            print(f"Patient with MRN: {patient_mrn} is not found ")    
          
    except Exception as exc:
        print("Error creating new prescription", exc)    

def update_prescription():
    rx_number = validate_input("Enter prescription number: ", "rx_number")
    if prescription := Prescription.find_by_id(rx_number):
        try:
            medication = input("Enter medication name: ")
            if len(medication) == 0:
                medication = prescription.medication    
            prescription.medication = medication
            quantity = validate_input("Enter medication quantity: ", "quantity")
            prescription.quantity = quantity
            refills = validate_input("Enter medication refills: ", "refills")
            prescription.refills = refills
            patient_mrn =  validate_input("Enter patient's mrn:  ", "patient mrn")
            prescription.patient_mrn = patient_mrn
            prescription.update()
            print(f'Successfully updated prescription.\n\t Precription rx_number: {prescription.rx_number}.\n\tMedication name: {presciption.medication}\n\tQty: {prescription.quantity}\n\tRefills: {prescription.refills}\n\tPatient\'s name: {patient.name}.')
        except Exception as exc:
            print(f'Error updating prescription: ', exc) 
    else:
        print(f'Prescription {rx_number} not found')

def delete_prescription():
    rx_number = validate_input("Enter prescription  number: ", "rx_number")
    if prescription := Prescription.find_by_id(rx_number):
        prescription.delete()
        print(f'Success {rx_number} deleted')
    else:
        print(f'Prescription {rx_number} not found')

def list_patient_prescriptions():
    mrn_number = validate_input("Enter patient's medical record number: ", "medical record number")
    if patient := Patient.find_by_mrn(mrn_number):
        for prescription in patient.prescriptions():
            print(f'Prescription:\n\tMedication name: {prescription.medication}.\n\tQty: {prescription.quantity}.\tRefills: {prescription.refills}.\n\tPatient\'s name: {patient.name}.')
    else:
        print(f'Patient {mrn_number} not found')                    

def exit_program():
    print("Goodbye!")
    exit()

def validate_input(prompt, property_name):
    inpt= input(prompt)
    while not inpt.isdigit() or int(inpt) <= 0 :
        print(f'{property_name} is not valid, try again')
        inpt = input(prompt)
    return int(inpt)