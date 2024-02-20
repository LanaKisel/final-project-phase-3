# Phase 3 CLI+ORM Project Template

## CLI
The CLI for this project is located in 'lib/cli.py'.
CLI is an interactive script, that prompts the user and performs
operations based on user input.
First thing you see when open cli file are imports of functions from 'lib/helper.py'. 
Aftet that I define main() function which has a while loop, calls menu() function, and elif statements.
The menu() function prints user's menu options. 
Based on the user's input, main() function  will perform an operation, corresponding to the if/elif statement.
Lastly, the if __name__ == '__main__' block tells the interpreter that this script should only be run if 'lib/cli.py' itself is being called from the command line.
You can run the CLI with `python lib/cli.py`

## HELPERS
The helper functions are located in `lib/helpers.py`.
First I import models.prescription and models.patient.
After I create functions: 
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
I created validate_input() function which takes in a propmpt(a message specific to the property) and a property_name(). This function checks if input is an integer and greater than 0. If not, it'll print a helpful message from prompt attribute, saying, the attribute property_name is not valid.       

## MODELS
This application has 2 models: patient.py and prescription.py.

### RELATIONSHIP
The modules have a one to many relationshop. A patient can have multiple prescriptions. 
 Patient_id is a foreign key in prescription.py. 

### PATIENT.PY 
patient.py creates a Patient object wich has name, surname, address and id properties. id defined as None at the begining because it's' created after the object is created in the database. 
 Then I have a few methods for writing to the databse:
create_table(cls), drop_table(cls), save(self), create(cls, name, surname, address), update(self), delete(self).
 And methods for reading from the database:
instance_from_db(cls, row), get_all(cls), find_by_id(cls, id), find_by_name(cls, name).
 And prescriptions(self) functions that return list of prescriptions associated with current patient.

### PRESCRIPTION.PY
Similarly to patient.py model, Prescription object has some attributes:  medication, quantity, refills, patient_id, id.
 Then methods for writing to the database: 
create_table(cls), drop_table(cls), save(self), create(cls, medication, quantity, refills, patient_id), update(self), delete(self). 
 And methods for reading from the database:
  instance_from_db(cls, row), get_all(cls), find_by_id(cls, id), find_by_name(cls, name).

## SEED.PY
seed.py file helps to seed database. It has imports from prescription and patient. It has seed_database() function,  which clears database every time its called and creates new objects. After executing seed_database(), prints a success message: "Seeded database".    