
#SOLVED
'''Question: Complete the script so that it removes duplicate'''

a = ["1",1,"1",2]

'''expected output: ['1', 2, 1]'''

b = []
for i in range(len( a)):
    if a[i] not in b:
        b.append(a[i])

print(a)
print(b)

#Their solution is as follows:

c = set(a)
d = list(c)
print(d)
#And with this variant the order of the items is suddenly clear now.
#Fuck.Again just a half point for me I guess...
'''Well, their solution is even sexier written as follows:
    a=list(set(a))
    print(a))
    sheeeeeeeeeeet...'''
