#SOLVED did not solve it,looked in the solution.no points for me
'''Question:
    Filter the dictionary by removing all items with a value greater than 1'''
    
d = {"a":1,"b":2,"c":3}
d = dict((key,value) for key,value in d.items() if value <=1)
print(d)