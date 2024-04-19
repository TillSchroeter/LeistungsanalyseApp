from my_functions import build_experiment, build_person
import json
from my_classes import Person, Experiment

'''print ('select your sex: 1 for male and 2 for female)')
x = input () 
if x == 1:
    sex_ = 'male'
if x == 2:
    sex_ = 'female'
print ('x ist gleich'+ x + sex_)'''

print ('Wähle dein Geschlecht aus (male or female):')
sex_ = input()
# sex_ = 'male'

print('Tippe deinen Vornamen ein:')
First_Name_ = input()
# First_Name_ = 'Till'

print('Tippe deinen Nachnamen ein:')
Last_Name_ = input()
# Last_Name_ ='Schroeter'

print ('Tippe dein alter ein:')
age_str  = input ()
age_int = int (age_str)
print (type(age_int))
# age_int = 20

print ('Was ist der Experimenten Name:')
Sporttest_ = input ()

print ('Wie ist das Datum:')
Datum_ = input ()

print ('Wer ist der Versuchsleiter:')
Versuchsleiter_ = input()

print ('welche Sprtart:')
Sportart_ = input ()

#Experiment_Dict = {'Person': build_person (First_Name_, Last_Name_, sex_, age_int), 'Experiment': build_experiment (Sporttest_, Datum_, Versuchsleiter_, Sportart_)}
#print (Experiment_Dict)

Data_Person = Person (First_Name_, Last_Name_, sex_, age_int)
Data_Experiment = Experiment (Sporttest_, Datum_, Versuchsleiter_, Sportart_)
Experiment_Dict2 = {'Person': Data_Person.return_Dict(), 'Experiment':  Data_Experiment.return_Dict()}
print (Experiment_Dict2)

with open("Functions_sample.json", "w") as outfile: 
    json.dump(Experiment_Dict2, outfile)


# Experiment1 = Experiment ('Sporttest', '15.04.2024', 'Hans Juergen Herrman', 'Volleyball' )
# Experiment1.test ()




