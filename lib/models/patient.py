from models.__init__ import CURSOR, CONN
class Patient:
    all = {}

    def __init__(self, name, surname, address, id = None):
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id
    
    def __repr__(self):
        return f"<Patient {self.id}: {self.name}, {self.surname}, {self.address}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise Exception("name must be a non empty string")

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        if isinstance(surname, str) and len(surname):
            self._surname = surname
        else:
            raise Exception("surname must be a non empty string")  

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if isinstance(address, str) and len(address):
            self._address = address
        else:
            raise Exception("address must be a non empty string")
            

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            address TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO patients (name, surname, address)
            VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.surname, self.address))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, surname, address):
        patient = cls(name, surname, address)
        patient.save()
        return patient

    def update(self):
        sql = """
            UPDATE patients
            SET name = ?, surname = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.surname, self.address, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM patients
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        # Check the dictionary for an existing instance using the row's primary key
        patient = cls.all.get(row[0])
        if patient:
            # ensure attributes match row values in case local instance was modified
            patient.name = row[1]
            patient.surname = row[2]
            patient.address = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            patient = cls(row[1], row[2], row[3])
            patient.id = row[0]
            cls.all[patient.id] = patient
        return patient

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM patients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM patients
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM patients
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def prescriptions(self):
        from models.prescription import Prescription
        sql = """
            SELECT * FROM prescriptions
            WHERE patient_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Prescription.instance_from_db(row) for row in rows]        