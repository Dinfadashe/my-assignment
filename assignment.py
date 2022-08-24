                                     #parent class

class student:
    def __init__(person, firstname, lastname, height):

                           #instance variables of the parent class 

         person.firstname = firstname
         person.lastname = lastname
         person.height = height
    
                      # method that returns all details for parent class object 

    def fullDetails(person): 
         return f'Firstname: {person.firstname}\nLastname: {person.lastname}\nheight: {person.height}\nRank: {person.rank}' 

                                       #child class (teacher) 

class Teacher(student): 
    def __init__(person, firstname, lastname, height, rank):
        super().__init__(firstname, lastname, height)
        person.rank = rank

                                    #attributes for child class 

Dinfa = Teacher('Dinfa', 'Dashe', 40, 10) 
Aminu = Teacher('Aminu', 'Salama', 45, 12)

print(Teacher.fullDetails(Dinfa))
print(Teacher.fullDetails(Aminu))