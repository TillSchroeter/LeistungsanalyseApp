import json
from datetime import datetime

class Person ():
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def return_Dict (self):
        return self.__dict__
    
    def safe (self):
        with open("Classes_Person_sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile)


class Subject (Person):

    def __init__ (self,first_name, last_name, sex, birth_date):
        super().__init__(first_name, last_name)
        self.sex = sex
        self.birth_date = birth_date
    
    def calculate_age (self):
            today = datetime.now()
            date = datetime.strptime(self.birth_date, '%d.%m.%Y')
            delta = today - date
            age = delta.days / 365.25 #Berücksichtigung des Schaltjahres
            age_rounded = round (age, 3)
            return age_rounded

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.calculate_age()
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.calculate_age()
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        max_hr_bpm = round (max_hr_bpm, 3)
        return (max_hr_bpm)

    def return_Dict (self):
        self.__dict__ ["estimate_max_hr"] = self.estimate_max_hr()
        self.__dict__ ["age"] = self.calculate_age ()
        del self.__dict__['birth_date']
        return self.__dict__


class Supervisor (Person):

    def __init__ (self, first_name, last_name):
        super().__init__(first_name, last_name)

    def return_Dict (self):
        return self.__dict__

'''Person1 = Subject ('Till', 'Schröter', 'male', '25.04.2003')
print (Person1.estimate_max_hr())
print (Person1.__dict__)
Person1.safe ()
print (Person1.return_Dict ())

Supervisor1 = Supervisor ('Hans', 'Jürgen')
# print (Supervisor1)'''


class Experiment ():

    def __init__ (self, experiment_name, date, subject):
       self.experiment_name = experiment_name
       self.date = date
       self.subject = subject
    
    def test (self):
        print('funktioniert')

    def return_Dict (self):
        return self.__dict__

    def safe (self):
       with open("Classes_Experiment_sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile)



