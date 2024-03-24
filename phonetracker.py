import phonenumbers

from myNo import number

from phonenumbers import geocoder

samNumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(samNumber, "en")
print(yourlocation)
