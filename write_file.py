
#open and append to a file called pelican.txt
open_file = open('pelican.txt', 'w')

#appending using the write method
firstline = open_file.write("A wonderful bird is the pelican, \n",)
open_file.close()

open_file = open('pelican.txt', 'a')
secondline = open_file.write("His bill holds more than his belican, \n")
open_file.close()

open_file = open('pelican.txt', 'a')
lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]
open_file.writelines(lines)
open_file.close()


f = open('pelican.txt', 'r')
for x in f:
    print(x, end='')
f.close()






