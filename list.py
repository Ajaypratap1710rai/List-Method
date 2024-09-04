my_list = [1, 2, 3]

my_list.append(4)
print("After append:", my_list)  

my_list.extend([5, 6])
print("After extend:", my_list)  

my_list.insert(2, 'a')
print("After insert:", my_list)  

my_list.remove('a')
print("After remove:", my_list)  

popped_item = my_list.pop()
print("Popped item:", popped_item)  
print("After pop:", my_list)  

count = my_list.count(3)
print("Count of 3:", count)  

my_list.sort(reverse=True)
print("After sort (desc):", my_list) 

my_list.reverse()
print("After reverse:", my_list)  

copied_list = my_list.copy()
print("Copied list:", copied_list)  
