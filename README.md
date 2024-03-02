# Phase 3 CLI+ORM Project Template
## SET up
pipenv install
pipenv shell
python lib/seed.py
python lib/cli.py

## CLI
The CLI for this project is located in 'lib/cli.py'.
CLI is an interactive script, that prompts the user and performs
operations based on user input.
The first thing you see when opening the cli file are imports of functions from 'lib/helper.py'and Figlet from pyfiglet, which helps me to render styled text. 
In main() I have my multi level menu. Depending on user inputs it performs a corresponding function. 
Lastly, the if __name__ == '__main__' block tells the interpreter that this script should only be run if 'lib/cli.py' itself is being called from the command line.
You can run the CLI with `python lib/cli.py`
Here's the menu options:
![Image of CLI menu options](/cli menu options-2.png)

## HELPERS
The helper functions are located in `lib/helpers.py`.
First I import models.prescription and models.patient.
After I create functions: 
    exit_program,
    list_patients,
    find_patient_by_name,
    find_patient,
    create_patient,
    update_patient, delete_patient,
    list_prescriptions,
    find_prescription,
    find_prescription_by_name,
    create_prescription,
    update_prescription,
    delete_prescription,
    list_patient_prescriptions,
    find_patient_by_prescription_id
I created validate_input() function which takes in a few parameters: a prompt (a message specific to the property), property_name(), minimum_value and a default_value, which is optional. This function checks if the input is an empty string, and in case of editing prescription or patient information, when empty string is entered the value defaults to the original value. It also checks if the input is an integer and if it's greater than minimum_value parameter. If not, it'll print a helpful message using the property_name attribute.

## MODELS
This application has 2 models: patient.py and prescription.py.

### RELATIONSHIP
The modules have a one-to-many relationship. A patient can have multiple prescriptions. 
 Patient_id is a foreign key in prescription.py. 

### PATIENT.PY 
patient.py creates a Patient object that has a name, surname, address, and id properties. id defined as None at the beginning because it's' created after the object is created in the database. 
 Then I have a few methods for writing to the database:
create_table(cls), drop_table(cls), save(self), create(cls, name, surname, address), update(self), delete(self).
 And methods for reading from the database:
instance_from_db(cls, row), get_all(cls), find_by_id(cls, id), find_by_name(cls, name), find_by_mrn(cls, mrn).
 And prescriptions(self) function that returns a list of prescriptions associated with a certain patient.

### PRESCRIPTION.PY
Similarly to patient.py model, Prescription object has some attributes:  medication, quantity, refills, patient_id, id.
 The methods for writing to the database: 
create_table(cls), drop_table(cls), save(self), create(cls, medication, quantity, refills, patient_id), update(self), delete(self). 
 And methods for reading from the database:
  instance_from_db(cls, row), get_all(cls), find_by_id(cls, id), find_by_name(cls, name), find_by_rx_name().

## SEED.PY
seed.py file helps to seed the database. It has imports from prescription and patient. It has seed_database() function,  which clears database every time it's called and creates new objects. After executing seed_database(), prints a success message: "Seeded database". 