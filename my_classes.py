import json

class Person ():
    
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        #print(max_hr_bpm)
        return int(max_hr_bpm)
    
    def return_Dict (self):
        self.__dict__ ["estimate_max_hr"] = self.estimate_max_hr()
        return self.__dict__
    
    def safe (self):
        self.__dict__ ["estimate_max_hr"] = self.estimate_max_hr()
        #print (self.__dict__)
        with open("Classes_Person_sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile)
        

Person1 = Person ('Tillll', 'Schroeter', 'male', 20)
# print (Person1.__dict__)
# Person1.estimate_max_hr ()
# Person1.safe()
# print (Person1.return_Dict ())


class Experiment ():

    def __init__ (self, experiment_name, date, supervisor, subject):
       self.experiment_name = experiment_name
       self.date = date
       self.supervisor = supervisor
       self.subject = subject
    
    def test (self):
        print('funktioniert')

    def return_Dict (self):
        return self.__dict__

    def safe (self):
       with open("Classes_Experiment_sample.json", "w") as outfile: 
            json.dump(self.__dict__, outfile)


#Experiment1 = Experiment ('Sporttest', '15.04.2024', 'Hans Juergen Herrman', 'Volleyball' )
#Experiment1.safe ()
#Experiment1.test ()

        













