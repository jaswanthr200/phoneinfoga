import phonenumbers
from phonenumbers import geocoder, carrier
from phonenumbers import timezone
#import sys
from termcolor import colored, cprint
import pyfiglet

title = pyfiglet.figlet_format("phoneinfoga")
titlex = colored(title, 'magenta', attrs=['bold'])
print(titlex)


ph = input("ENTER THE TARGET PHONE NUMBER WITH COUNTRY CODE:")
phone_number = phonenumbers.parse(ph)

location = colored(timezone.time_zones_for_number(phone_number) ,'red', attrs=['bold'])

carr = colored(carrier.name_for_number(phone_number, 'en'), 'red', attrs=['bold'])

geo = colored(geocoder.description_for_number(phone_number, 'en'), 'red', attrs=['bold'])

valid = colored(phonenumbers.is_valid_number(phone_number), 'red', attrs=['bold'])


l = colored("LOCATION OF THE TARGET:", 'green', attrs=['bold'])

c = colored("INTERNET SERVICE PROVIDER:", 'green', attrs=['bold'])

g = colored("COUNTRY:", 'green', attrs=['bold'])

v = colored("VALID NUMBER:", 'green', attrs=['bold'])


z = colored("**********************************************************************", 'yellow', attrs=['bold'])

print(z)
print('')
print(l + str(location))
print('')
print(c + str(carr))
print('')
print(g + str(geo))
print('')
print(v + str(valid))
print('')
print(z)