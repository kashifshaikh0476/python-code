#insert data
list1=[1,2,3,4,5]
print(list1)

#accessing data
list1[1]
print(list1[1])

list1[1:3]
print(list1[1:3])

#update data
list1[0]=10
print(list1)

#add data using append
list1.append(6)
print(list1)

#add data using extend
list1.extend([7,8])
print(list1)

#addition of two list
list2=[9,10]
print(list2)

list3=list1+list2
print(list3)

#insert in list 1
list1.insert(1,1)
print(list3)

#delete  element
del list1[0]
print(list1)

list1.remove(8)
print(list1)


# Compare the two lists
if list1 == list2:
    print("The lists are equal.")
elif list1 < list2:
    print("list1 is less than list2.")
else:
    print("list1 is greater than list2.")

print(list1, list2)

#to find the length
len(list1)
print("length is: ",len(list1))

#to find maxmum
print("max is: ",max(list1))

#to find min
print("min is: ",min(list1))