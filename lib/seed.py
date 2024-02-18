#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.prescription import Prescription
from models.patient import Patient
# from faker import Faker
# import random
#fake = Faker()

def seed_database():
    Prescription.drop_table()
    Patient.drop_table()
    Patient.create_table()
    Prescription.create_table()

    lilly = Patient.create("Lilly", "Jefferson", "982 Fadel Overpass Suite 578")
    paul = Patient.create("Paul", "Griffin", "5167 Boyle Plains")
    #ondansetron = Prescription.create() 
    
seed_database()
print("Seeded database")    
    
    # p1 = Patient.create(fake.name(), fake.surname(), fake.address())
    # p2 = Patient.create(fake.name(), fake.surname(), fake.address())

    # patients = [
    #     Patient(
    #         name = fake.name(),
    #         surname = fake.surname(),
    #         address = fake.address()
    #     )
    # for i on range(12)]
