from my_functions import build_experiment
from my_functions import build_person
import json

'''print ('select your sex: 1 for male and 2 for female)')
x = input () 
if x == 1:
    sex_ = 'male'
if x == 2:
    sex_ = 'femala'
print ('x ist gleich'+ x + sex_)'''

print ('Wähle dein Geschlecht aus (male or female):')
sex_ = input()

print('Tippe deinen Vornamen ein:')
First_Name_ = input()

print('Tippe deinen Nachnamen ein:')
Last_Name_ = input()

print ('Tippe dein alter ein:')
age_str  = input ()
age_int = int (age_str)
#print (type(age_int))

print ('Was ist der Experimenten Name:')
Sporttest_ = input ()

print ('Wie ist das Datum:')
Datum_ = input ()

print ('Wer ist der Versuchsleiter:')
Versuchsleiter_ = input()

print ('welche Sprtart:')
Sportart_ = input ()

Experiment_Dict = {'Person': build_person (First_Name_, Last_Name_, sex_, age_int), 'Experiment': build_experiment (Sporttest_, Datum_, Versuchsleiter_, Sportart_)}
print (Experiment_Dict)

with open("sample.json", "w") as outfile: 
    json.dump(Experiment_Dict, outfile)







