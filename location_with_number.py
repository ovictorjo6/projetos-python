import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input('Enter any number to check location: ')
ch_number = phonenumbers.parse(number,'CH')

print(geocoder.description_for_number(ch_number,'en'))

s_num = phonenumbers.parse(number,'RO')
print(carrier.name_for_number(s_num,'en'))
