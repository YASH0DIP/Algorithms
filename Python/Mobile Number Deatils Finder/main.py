import phonenumbers #write on cmd "pip install phonenumbers" install in which folder where your project lies.
from phonenumbers import geocoder
from phonenumbers import carrier
num="+" + input("Enter Country Code :")
ber=input("Enter Mobile Number :")

ch_nmber = phonenumbers.parse(num+ber, "CH") #Passing Number and Country
print(geocoder.description_for_number(ch_nmber, "en")) #Printing Country Which Number Belongs to


service_nmber = phonenumbers.parse(num+ber, "RO") #Passing Service provider
print(carrier.name_for_number(service_nmber,"en")) #Printing Service Provider of given Number
