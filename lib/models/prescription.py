from models.__init__ import CURSOR, CONN
from models.patient import Patient

class Prescription:

    all={}

    def __init__(self, medication, quantity, refills, patient_mrn, id = None):
        self.medication = medication
        self.quantity = quantity
        self.refills = refills 
        self.patient_mrn = patient_mrn
        self.id = id

        #Prescriptions.all.add(self)
    def __repr__(self):
        return f"<Prescription {self.id}: {self.medication}, {self.quantity}, {self.refills}, {self.patient_mrn}>"    
        


    @property
    def medication(self):
        return self._medication

    @medication.setter
    def medication(self, medication):
        if isinstance(medication, str) and len(medication):
            self._medication = medication
        else:
            raise Exception("Medication must be a non empty string")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        if isinstance(quantity, int) and quantity > 0:
            self._quantity = quantity
        else:
            raise Exception("quantity must be integer with a value more than 0") 

    @property
    def refills(self):
        return self._refills

    @refills.setter
    def refills(self, refills):
        if isinstance(refills, int):
            self._refills = refills
        else:
            raise Exception('refills must be integer')

    @property
    def patient_mrn(self):
        return self._patient_mrn

    @patient_mrn.setter
    def patient_mrn(self, patient_mrn):
        if type(patient_mrn) is int and Patient.find_by_id(patient_mrn):
            self._patient_mrn = patient_mrn
        else:
            raise Exception("patient_mrn must reference patient in the database")              

    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS prescriptions (
            rx_number INTEGER PRIMARY KEY,
            medication TEXT,
            quantity INTEGER,
            refills INTEGER,
            patient_mrn INTEGER,
            FOREIGN KEY (patient_mrn) REFERENCES patients(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS prescriptions;
        """    
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO prescriptions (medication, quantity, refills, patient_mrn )
            VALUES (?,?,?,?)
        """
        CURSOR.execute(sql, (self.medication, self.quantity, self.refills, self.patient_mrn))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        sql = """
            UPDATE prescriptions
            SET medication = ?, quantity = ?, refills = ?, patient_mrn = ?
            WHERE id = ?
        """    
        CURSOR.execute(sql, (self.medication, self.quantity, self.refills, self.patient_mrn, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM prescriptions
            WHERE id = ?
        """    
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, medication, quantity, refills, patient_mrn):
        prescription = cls(medication, quantity, refills, patient_mrn)
        prescription.save()
        return prescription

    @classmethod
    def instance_from_db(cls, row):
        prescription = cls.all.get(row[0])
        if prescription:
            prescription.medication = row[1]
            prescription.quantity = row[2]
            prescription.refills = row[3]
            prescription.patient_mrn = row[4]
        else:
            prescription = cls(row[1], row[2], row[3], row[4])
            prescription.id = row[0]
            cls.all[prescription.id] = prescription   
        return prescription

    @classmethod
    def get_all(cls):
        sql= """
            SELECT *
            FROM prescriptions
        """             
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]    
    
                       
    @classmethod
    def find_by_id(cls, id):
        sql="""
            SELECT *
            FROM prescriptions
            WHERE id = ?
        """             
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, medication):
        sql = """
            SELECT * 
            FROM prescriptions
            WHERE medication is ?
        """
        row = CURSOR.execute(sql, (medication,)).fetchone()
        return cls.instance_from_db(row) if row else None