from address import Address
from mailing import Mailing

to_address = Address("141021", "Мытищи", "Лётная", 46, 57)
from_address = Address("143405", "Красногорск", "Зверева", 6, 101)

mailing = Mailing(to_address, from_address, 1000, "mov25485145")

print(mailing)
