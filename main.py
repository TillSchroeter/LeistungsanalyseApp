from my_functions import build_experiment, build_person
import json
from my_classes import Person, Subject, Supervisor, Experiment

print ('Wähle dein Geschlecht aus (male oder female):')
sex_ = input()

print('Tippe deinen Vornamen ein:')
First_Name_ = input()

print('Tippe deinen Nachnamen ein:')
Last_Name_ = input()

print ('Tippe dein geburtsdatum in folgener Form ein "dd.mm.yyyy":')
geburtsdatum_ = input()

print ('Was ist der Experimenten Name:')
Sporttest_ = input ()

print ('Wie ist das heutige Datum:')
Datum_ = input ()

print ('Wie ist der Vorname des Versuchsleiters:')
Versuchsleiter_vorname_ = input()
print ('Wie ist der Nachname des Versuchsleiters:')
Versuchsleiter_nachname_ = input()

print ('Welche Sportart wird ausgeübt:')
Sportart_ = input ()


Data_Person = Subject (First_Name_, Last_Name_, sex_, geburtsdatum_)
Data_Experiment = Experiment (Sporttest_, Datum_, Sportart_)
Data_Versuchsleiter = Supervisor (Versuchsleiter_vorname_, Versuchsleiter_nachname_)
Experiment_Dict2 = {'Person': Data_Person.return_Dict(), 'Versuchsleiter': Data_Versuchsleiter.return_Dict(), 'Experiment':  Data_Experiment.return_Dict()}
print (Experiment_Dict2)

with open("Functions_sample.json", "w") as outfile: 
    json.dump(Experiment_Dict2, outfile)





