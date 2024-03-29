import phonenumbers
from phonenumbers import geocoder

ph1 = phonenumbers.parse("+917294536271")
ph2 = phonenumbers.parse("+919407411278")
ph3 = phonenumbers.parse("+12136574429")
ph4 = phonenumbers.parse("+919329812531")

print("locations\n")
print(geocoder.description_for_number(ph1,"en"))
print(geocoder.description_for_number(ph2,"en"))
print(geocoder.description_for_number(ph3,"en"))
print(geocoder.description_for_number(ph4,"en"))