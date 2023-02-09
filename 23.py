#Question: Access the third value of key b  from the dictionary.
from pprint import pprint
my_dick = {"a":list(range(1,11)),"b":list(range(11,21)),"c":list(range(21,31))}
pprint(my_dick)
pprint(my_dick["b"],2)
