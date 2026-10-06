 # Patient class
class Patient:
    def __init__(self, Patient_id, name, age, gender, diagnosis):
        self.name = name
        self.Patient_id = Patient_id
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis

    def display_info(self):
        print(f"\n***** Patient information *****")
        print(f"ID: {self.Patient_id}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")
        print(f"gender:{self.gender}")
        print(f"diagnosis{self.diagnosis}")

# Hospital class


class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name

        self.patients =[]

    def add_patient(self, patient):
        self.patients.append(patient)
        print("Patient added successfully")

    def display_Patient(self):
        print("\n ******* All Patient ********")
        print(F"\n ******** {self.hospital_name}*******")

        # Check if there are Patients
        if len(self.patients) == 0:
            print("No Patient Records Found")
        else:
            for patient in self.patients:
                patient.display_info()

# Patient objects
Patient1 = Patient(101, "jalloh", 23, "Male", "Poverty")
Patient2 = Patient(102, "wurie", 24, "Male", "Malaria")
Patient3 = Patient(103, "fallu", 27, "Male", "Headache")

# Hospital objects
hospital1 = Hospital("Juldeh Clinic")

# Add patient to the hospital using add_Patient method in the hospital
hospital1.add_patient(Patient1)
hospital1.add_patient(Patient2)
hospital1.add_patient(Patient3)

# Display all patient records in the hospital
hospital1.display_Patient()

