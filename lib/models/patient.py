from models.__init__ import CURSOR, CONN
class Patient:
    all = {}

    def __init__(self, name, surname, address, id = None):
        self.name = name
        self.surname = surname
        self.address = address
        self.id = id

        #Patients.all.append(self)
    
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
        """ Create a new table to persist the attributes of Patient instances """
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
        """ Drop the table that persists Patient instances """
        sql = """
            DROP TABLE IF EXISTS patients;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, surname, address values of the current Patient instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
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
        """ Initialize a new Patient instance and save the object to the database """
        patient = cls(name, surname, address)
        patient.save()
        return patient

    def update(self):
        """Update the table row corresponding to the current Patient instance."""
        sql = """
            UPDATE patients
            SET name = ?, surname = ?, address = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.surname, self.address, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Patient instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM patients
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Department object having the attribute values from the table row."""

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
        """Return a list containing a Patient object per row in the table"""
        sql = """
            SELECT *
            FROM patients
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a Patient object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM patients
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a Patient object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM patients
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def prescriptions(self):
        """Return list of prescriptions associated with current patient"""
        from models.prescription import Prescription
        sql = """
            SELECT * FROM prescriptions
            WHERE patient_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [Prescription.instance_from_db(row) for row in rows]        