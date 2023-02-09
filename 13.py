#SOLVED
'''Complete the script,so it gereates the expected output using "my_range"as input data
Please note that the items of the expected list output are all strings.
my_range = range(1,21)
Expected Output:
    ['1','2','3', etc]
    '''

my_range = range(1,21)
#MySolution
print(list(i for i in my_range))

#correctsolution
print(list(map(str,my_range)))
'''Didnt see that it doesnt print string numbers.fuck.Ill take the half point from before...'''
