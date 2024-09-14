#comment in python
txt = "i am a blessed man to have met onma"
if "onme" in txt:
     print("yes,she is my wife")
else: 
     print("yes,she is not my wife")

text = 'Hello world'
print(text.split(","))
print(text.upper())
print(text[-1:-6])
a = 34
b = "JSS2"
c = "James Igoche"
d = f' i will be {a*3}yrs in 3yrs time {b} by name {c}'
print(str(d))
A = [2,3,5]
a = [6,7,8,9,10]
a.extend(A)
print(a)
a[1:2] =["lawrence","Onma","uja"]
print(a)
for y in a:
 print(y)

Onma = {
    "car" : "Honda",
    "color" : "black",
    "version":24,
}
print(len(Onma["color"]))

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car

print(x) #before the change

car["color"] = "white"

print(x) #after the change
