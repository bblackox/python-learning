marks = {
    "Rohan": 100,
    "Blacky": 98,
    "Shyam": 34,
    "Harry": 0
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Rohan":99 , "Shilpa": 95})
print(marks)

print(marks.get("Harry"))