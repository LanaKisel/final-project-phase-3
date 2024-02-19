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
    id_ = input("Enter patient's id: ")
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
    id_ = input("Enter patient's id: ")
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
    id_ = input("Enter patient's id: ")
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
    id_ = input("Enter prescription id: ")
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
    id_ = input("Enter prescription's id: ")
    if prescription := Prescription.find_by_id(id_):
        try:
            medication = input("Enter medication name: ")
            prescription.medication = medication
            quantity = int(input("Enter medication quantity: "))
            prescription.quantity = quantity
            refills = int(input("Enter prescription refills: "))
            prescription.refills = refills
            patient_id = int(input("Enter patient's id: "))
            prescription.patient_id = patient_id
            prescription.update()
            print(f'Success: {prescription}')
        except Exception as exc:
            print(f'Error updating prescription: ', exc) 
    else:
        print(f'Prescription {id_} not found')

def delete_prescription():
    id_ = input("Enter prescription id: ")
    if prescription := Prescription.find_by_id(id_):
        prescription.delete()
        print(f'Success {id_} deleted')
    else:
        print(f'Prescription {id_} not found')

def list_patient_prescriptions():
    id_ = input("Enter patient's id: ")
    if patient := Patient.find_by_id(id_):
        for prescription in patient.prescriptions():
            print(prescription)
    else:
        print(f'Patient {id_} not found')                    

def exit_program():
    print("Goodbye!")
    exit()
