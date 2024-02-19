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
    id_ = validate_input("Enter patinet's id: ", "id")       
    patient = Patient.find_by_id(id_)
    print(patient) if patient else print(        
    f'Patient {id_} not found')


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
    id_ = validate_input("Enter patinet's id: ", "id")
    if patient := Patient.find_by_id(id_):
        try:
            name = input("Enter patient's name: ")
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
        print(f'Patient {id_} not found')    

def delete_patient():
    id_ = validate_input("Enter patinet's id: ", "id")
    if patient := Patient.find_by_id(id_):
        patient.delete()
        print(f'Success {id_} deleted')
    else:
        print(f'Patient {id_} not found')

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
    id_ = validate_input("Enter prescription  id: ", "id")
    prescription = Prescription.find_by_id(id_)
    print(prescription) if prescription else print(
        f'Prescription {id_} not found')

def create_prescription():
    medication = input("Enter medication name: ")
    quantity = int(input("Enter quantity of medication: "))
    refills = int(input("Enter presciption's refills: "))
    patient_id = int(input("Enter patient_id: "))


    try:
        presciption= Prescription.create(medication, quantity, refills, patient_id)
        print(f'Success: {presciption}')
    except Exception as exc:
        print("Error creating new prescription", exc)    

def update_prescription():
    id_ = validate_input("Enter rescription  id: ", "id")
    
    if prescription := Prescription.find_by_id(id_):
        try:
            medication = input("Enter medication name: ")
            prescription.medication = medication
            quantity = validate_input("Enter medication quantity: ", "quantity")
            prescription.quantity = quantity
            refills = validate_input("Enter medication refills: ", "refills")
            prescription.refills = refills
            patient_id =  validate_input("Enter patient's id:  ", "patient id")
            prescription.patient_id = patient_id
            prescription.update()
            print(f'Success: {prescription}')
        except Exception as exc:
            print(f'Error updating prescription: ', exc) 
    else:
        print(f'Prescription {id_} not found')

def delete_prescription():
    id_ = validate_input("Enter rescription  id: ")
    if prescription := Prescription.find_by_id(id_):
        prescription.delete()
        print(f'Success {id_} deleted')
    else:
        print(f'Prescription {id_} not found')

def list_patient_prescriptions():

    if patient := Patient.find_by_id(id_):
        for prescription in patient.prescriptions():
            print(prescription)
    else:
        print(f'Patient {id_} not found')                    

def exit_program():
    print("Goodbye!")
    exit()

def validate_input(prompt, property_name):
    inpt= input(prompt)
    while not inpt.isdigit() or int(inpt) <= 0 :
        print(f'{property_name} is not valid, try again')
        inpt = input(prompt)
    return int(inpt)
