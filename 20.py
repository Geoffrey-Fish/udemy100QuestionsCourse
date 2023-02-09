#SOLVED anyway, half point less taken
'''Calculate the sum of all Dictionary Items'''

d = {"a":1,"b":2,"c":3}

print(d["a"]+d["b"]+d["c"])
#they fucked with me again.
#this time, the solution was as follows:
print(sum(d.values()))
