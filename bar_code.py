from barcode import EAN13
from barcode.writer import ImageWriter

#input your number here as a string
#tam 12
number = '123456789012'

my_code = EAN13(number, writer=ImageWriter())
my_code.save('new_code1')
