def order_list(my_list):
    ordered_list=[]
    i=0
    while i<len(my_list):
        min_l=min(my_list[i:])
        my_list.remove(min_l)
        my_list.insert(i, min_l)
        i+=1
    return my_list

def order_list2(my_list):
	for j in range(len(my_list)-1):
		for i in range(len(my_list)-1):
			if my_list[i]>my_list[i+1]:
				my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
	return my_list

list1=[125,65, 78,1,24,44]
list2=order_list2(list1)
print(list2)