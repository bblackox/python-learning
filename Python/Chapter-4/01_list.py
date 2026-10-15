friends = ["Apple","Orange",5,59.4,False,"Aakash","Rohan"]

print(friends[0])
friends[0] = "banana" #Unlike strings lists are mutable

print(friends[0])
print(friends[1:4])

# Any data type can be stored in the list

l1 = [6,5,7,4,3,5,9]
#l1.sort()
#l1.reverse()
l1.insert(3,44334)
print(l1)

l1.remove(6)
print(l1)