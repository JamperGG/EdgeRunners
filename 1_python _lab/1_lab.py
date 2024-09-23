from datetime import date

name = "Юра"
birth_year = 2006
current_year = date.today().year
age = current_year - birth_year

if age >= 18:
    status = "Повнолітній"
else:
    status = "Неповнолітній"

print(f"{name} є {age} років і він/вона вважається {status}.")
