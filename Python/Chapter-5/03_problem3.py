'''What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s))

#it returns the length of the set is equal to "2" because in python after comparing the int and flote value if they are same it return "1" it does not depend on the dataType