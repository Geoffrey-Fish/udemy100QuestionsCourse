#Question: Complete the script so that it produces the expected output. Please use my_range  as input data.

my_range = range(10,210,10)

 #Expected output: 

#[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200] 

print(list(my_range))

#what he wanted was the following:
my_range = range(1,21) # I shouldn t have touched this one, he SAID it is input data!!!!!

print([10* x for x in my_range])
#Tadaa! This works like a charm.
#Iĺl give a half point for ingenuity
