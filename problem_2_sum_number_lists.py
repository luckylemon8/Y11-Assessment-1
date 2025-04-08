def sum_number_lists(list1, list2):  
    min_length = min(len(list1), len(list2))  
    result = []  
    for i in range(min_length):  
        result.append(list1[i] + list2[i])

    return result  

list1 = [1, 2, 3]  
list2 = [4, 5, 6]  
result = sum_number_lists(list1, list2)  
print(result) 