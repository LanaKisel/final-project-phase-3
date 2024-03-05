#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.prescription import Prescription
from models.patient import Patient

def seed_database():
    Prescription.drop_table()
    Patient.drop_table()
    Patient.create_table()
    Prescription.create_table()

    lilly = Patient.create("Lilly", "Jefferson", "982 Fade Overpass Suite 578", 134597)
    paul = Patient.create("Paul", "Griffin", "5167 Boyle Plains", 345086)
    ondansetron = Prescription.create("ondansetron", 30, 3, 1)
    metronidazole = Prescription.create("metronidazole", 7, 0, 1)
    amoxicillin = Prescription.create("amoxicillin", 21, 0, 2)
    ibuprofen = Prescription.create("ibuprofen", 30, 3, 2 ) 
    
seed_database()
print("Seeded database")    