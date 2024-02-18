# lib/helpers.py
from models.prescription import Prescription
from models.patient import Patient

def list_patients():
    patients = Patient.get_all()
    for patient in patients:
        print(patient)

def find_patient_ny_name():
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

    


def exit_program():
    print("Goodbye!")
    exit()
