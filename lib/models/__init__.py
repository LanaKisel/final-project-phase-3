import sqlite3

CONN = sqlite3.connect('prescriptions.db')
CURSOR = CONN.cursor()
