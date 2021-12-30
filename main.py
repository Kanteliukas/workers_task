import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///Workers_database.db")
Base = declarative_base()

class Workers_database(Base):
    __tablename__ = "Workers_database"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    date_of_birth = Column("Date_of_birth", String)
    position = Column("Position", String)
    salary = Column("Salary", Float)
    first_day_at_work = Column("First_day_at_work", DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, surname, date_of_birth, position, salary):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.position = position
        self.salary = salary

    def __repr__(self):
        return (f"""({self.id}, {self.name}, {self.surname}, {self.date_of_birth} - 
{self.position}, {self.salary}: {self.first_day_at_work})""")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_worker_to_db():
    name_entry = input("Enter name: ")
    surname_entry = input("Enter surname: ")
    date_of_birth_entry = input("Enter date of birth (YYYY-MM-DD): ")
    position_entry = input("Enter employee's position: ")
    salary_entry = input("Enter salary: ")
    new_employee = Workers_database(name=name_entry,
                                        surname=surname_entry,
                                        date_of_birth=date_of_birth_entry,
                                        position=position_entry,
                                        salary=salary_entry)

    session.add(new_employee)
    session.commit()
    return f"Added"

def get_employee_to_work_with():
    employee_id = input("Enter employee's ID: ")
    employee_id = int(employee_id)
    employee = session.query(Workers_database).get(employee_id)
    return employee

def get_workers():
    user_reference = input("Do you wish to get all employees information? Yes/No: ")
    if user_reference.lower() == "no":
        employees_information = get_employee_to_work_with()
        return  employees_information
    else:
        all_employees = session.query(Workers_database).all()
        return all_employees

def update_workers_information():
    employee_to_update = get_employee_to_work_with()
    user_preference = input("""    1. Name
    2. Surname
    3. Date of birth
    4. Employee's position
    5. Salary
    Select which information to udpate: """)
    user_preference = int(user_preference)
    update_information_to = input("""Enter new information: """)
    if user_preference == 1:
        employee_to_update.name = update_information_to
    elif user_preference == 2:
        employee_to_update.surname = update_information_to
    elif user_preference == 3:
        employee_to_update.date_of_birth = update_information_to
    elif user_preference == 4:
        employee_to_update.position = update_information_to
    elif user_preference == 5:
        employee_to_update.salary = update_information_to
    session.commit()
    return employee_to_update

def delete_worker():
    employee_to_delete = get_employee_to_work_with()
    session.delete(employee_to_delete)
    session.commit()
    return f"Deleted"

def main():
    user_selection = input("""    1. Add worker to database
    2. Get employee/s
    3. Update employee's information
    4. Delete employee from Database
    Select option to start: """)
    user_selection = int(user_selection)
    if user_selection == 1:
        print(add_worker_to_db())
    elif user_selection == 2:
        print(get_workers())
    elif user_selection == 3:
        print(update_workers_information())
    elif user_selection == 4:
        print(delete_worker())

if __name__ == '__main__':
    main()


