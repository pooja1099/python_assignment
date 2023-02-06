
# Python3 code to demonstrate working of
# Remove records if Key not present
# Using list comprehension + keys()
 
# initializing list
list1 = [{'abc' : 1, 'def' : 3},
             {'pqr' : 3, 'xyz' : 5},
             {'rst' : 3}]
 
# printing original list
print("The original list : " + str(list1))
 
# initializing K Key
K = 'abc'
res = [ele for ele in list1 if K in ele.keys()]
         
# print result
print("List new list : " + str(res))