num_tuple=("1","2","3","4")
#tuples are immutable so that is why we areconeverting tuple to list and changing the list
# again converting list to tuple
num_list=list(num_tuple) #converting tuple to list
num_list.append("5") #addding value to the list
num_tuple=tuple(num_list) #converting list to tuple
print(num_tuple)
print(num_list)