#select odd index element from list1 and even index element from list2
#then print itn into list3
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
print("list1:",list1)
print("list2:", list2)
res = list()

odd_elements = list1[1::2]
print("Element at odd index position:")
print(odd_elements)

even_elements = list2[0::2]
print("Element at even index postion:")
print(even_elements)

print("Printing Final third list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)