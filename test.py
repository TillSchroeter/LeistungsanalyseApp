from datetime import datetime


def calculate_age (birth_date):
    today = datetime.now()
    date = datetime.strptime(birth_date, '%d.%m.%Y')
    delta = today - date
    age = delta.days / 365.25 #Berücksichtigung des Schaltjahres
    return age

print (calculate_age ('30.04.2003'))


