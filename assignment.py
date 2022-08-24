                                     #parent class

class student:
    def __init__(person, firstname, lastname, age):

                           #instance variables of the parent class 

         person.firstname = firstname
         person.lastname = lastname
         person.age = age
    
                      # method that returns all details for parent class object 

    def fullDetails(person): 
         return f'Firstname: {person.firstname}\nLastname: {person.lastname}\nage: {person.age}\nRank: {person.rank}' 

                                       #child class (teacher) 

class Teacher(student): 
    def __init__(person, firstname, lastname, age, rank):
        super().__init__(firstname, lastname, age)
        person.rank = rank

                                    #attributes for child class 

Dinfa = Teacher('Dinfa', 'Dashe', 40, 10) 
Aminu = Teacher('Aminu', 'Salama', 45, 12)

print(Teacher.fullDetails(Dinfa))
print(Teacher.fullDetails(Aminu))