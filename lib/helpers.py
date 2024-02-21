# lib/helpers.py
from models.prescription import Prescription
from models.patient import Patient

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter patient's name: ")
    patient = Patient.find_by_name(name)
    print(patient) if patient else print(
        f'Patient {name} not found')

def find_patient_by_id():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")       
    patient = Patient.find_by_id(mrn_number)
    print(patient) if patient else print(        
    f'Patient {mrn_number} not found')


def create_patient():
    name = input("Enter patient's name: ")
    surname = input("Enter patient's surname: ")
    address = input("Enter patient's address: ")
    try:
        patient = Patient.create(name, surname, address)
        print(f'Success: {patient}')
    except Exception as exc:
        print("Error creating patient: ", exc)

def update_patient():
    mrn_number = validate_input("Enter patient's medical record number: ", "medical record number")
    if patient := Patient.find_by_id(mrn_number):
        try:
            name = input("Enter patient's name: ")
            if len(name) == 0:
                name = patient.name
            patient.name = name
            surname = input("Enter patient's surname: ")
            patient.surname = surname
            address = input("Enter patient's address: ")
            patient.address = address
            patient.update()
            print(f'Success: {patient}')
        except Exception as exc:
            print("Error updating patient: ", exc)
    else:
        print(f'Patient {mrn_number} not found')    

def delete_patient():
    mrn_number = validate_input("Enter patinet's medical record number: ", "medical record number")
    if patient := Patient.find_by_id(mrn_number):
        patient.delete()
        print(f'Success {mrn_number} deleted')
    else:
        print(f'Patient {mrn_number} not found')

def list_prescriptions():
    prescriptions = Prescription.get_all()
    for prescription in prescriptions:
        print(prescription)

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
        presciption= Prescription.create(medication, quantity, refills, patient_mrn)
        print(f'Success: {presciption}')
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
            print(f'Success: {prescription}')
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
    rx_number = validate_input("Enter patient's medical record number: ", "medical record number")
    if patient := Patient.find_by_id(rx_number):
        for prescription in patient.prescriptions():
            print(prescription)
    else:
        print(f'Patient {rx_number} not found')                    

def exit_program():
    print("Goodbye!")
    exit()

def validate_input(prompt, property_name):
    inpt= input(prompt)
    while not inpt.isdigit() or int(inpt) <= 0 :
        print(f'{property_name} is not valid, try again')
        inpt = input(prompt)
    return int(inpt)

# def validate_input(prompt, property_name):
#     inpt= input(prompt)
#     while not inpt.isdigit() or 0 <=int(inpt) > 6:
#         print(f'{property_name} is not valid, try again')
#         inpt = input(prompt)
#     return int(inpt)
