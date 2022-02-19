import re

file = open('pelican.txt')
slurp = file.read()
file.close()

print(slurp)
print(type(slurp))

def stringconversion(string):
    typelist = list(string.split(","))
    return typelist

slurp_list = stringconversion(slurp)

print(type(slurp_list))
print(slurp_list)
print(len(slurp_list))

slurp_list2 = []

for x in slurp_list:
    slurp_list2.append(x.strip(" "))
    print(x)

#for x in slurp_list2:
        #print(x)


file.close()