from testhelper import test

list3 = []

def sum_number_lists(list1, list2):
        for i in list1:
            list3.append(i)
        for c in list2:
            list3.append(c)
        return(list3)

print(c)
print(i)
print(list3)

### TESTS - Run the code that calls the function to check it works.
test("Sum number lists 1", [4,5,7,8,10,11,13], sum_number_lists([1,2,3,4,5,6,7], [3,3,4,4,5,5,6]))
test("Sum number lists 2", [11,12,13,14,15,16,17], sum_number_lists([1,2,3,4,5,6,7], [10,10,10,10,10,10,10]))
