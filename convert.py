# Access values of dict() inside a list

foods = {
    'fruits': ['Apple', 'Orange', 'Grapes'],
    'vegetables': ['Tomato', 'Potato', 'Carrot']
}
print(foods['fruits'])
print(foods['vegetables'])


# Access values of list inside a dict()

def Convert(lst):
	dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
	return dct
  
lst = ['a', 1, 'b', 2, 'c', 3]
print(Convert(lst))

 
