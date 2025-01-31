list_1 = [1,2,3,4,5] 
print("Original list:", list_1)
n_splits = 2
list_1 = (list_1[len(list_1) - n_splits:len(list_1)] + list_1[0:len(list_1) - n_splits]) 
print("Rotated list:", list_1)
