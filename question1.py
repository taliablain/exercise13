cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']

#this method adds 'O' 'k' 'e' to the list instead of the whole word
#cheese += 'Oke'

#this is one correct way of adding an element to a list
cheese.append('Oke')
print(cheese)

#to add two elements at once
cheese.extend(['Red Leicester', 'Mozzarella'])
print(cheese)