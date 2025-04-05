### string – example of sequence ###

text = "Python is cool"
print(text)
print(type(text))

# indices
print(text[0])
print(text[-1])
print(text[len(text)-1])

# slices
print(text[0:6])
print(text[:6])
print(text[7:])

print(text[0:6:2])
print(text[6:0:-2])
print(text[-1::-1])

### immutable vs mutable types ###

# string - immutable
print(text.lower())
print(text)

text = text.lower()
print(text)
text = text.capitalize()
print(text)

# tuple - immutable type
1, 8, 9
triple = (10, 9, 5)
print(triple, type(triple))
print(triple.index(10))
print(triple.count(10))

# list - mutable type
values = [4, 7, 8, 10, 5, 4]
names = ["Ann", "Nick", "Ben", "George", "James"]
mixed = [23, 25, "no answer", 32]
print(values)
print(names)
print(mixed)

values[-1] = 30
print(values)

values.append(100)
print(values)

values.extend([90, 120])
print(values)

### assignment =, copy and deepcopy ###

# = for mutable types 
values2 = values
values2.append(100)
print(values, values2)

# copy() for mutable types
values3 = values.copy() 
values3.sort()
print(values)
print(values3)

test = [[1, 0, 1], 
        [0, 0, 0]]
test2 = test.copy()
print("До:", test, test2, sep = "\n")
test[1][0] = 1
print("После:", test, test2, sep = "\n")

# deepcopy for mutable types
from copy import deepcopy

test = [[1, 0, 1], 
        [0, 0, 0]]
test2 = deepcopy(test)
print("До:", test, test2, sep = "\n")

test[1][0] = 1
print("После:", test, test2, sep = "\n")

# = and copy for immutable types
whisper = "hey"
shout = whisper
shout = shout.upper()
print(whisper, shout)
