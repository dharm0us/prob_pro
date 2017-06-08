#iterate like a native
# https://www.youtube.com/watch?v=EnSu9hHGq5o
myList = ["The", "earth", "revolves", "around", "sun"]
for v in myList: #Look ma, no integers
    print(v)

#iterator is reponsible for producing the stream
#for string it's chars

for c in 'Hello':
    print(c)

d = {'a' : 1, 'b' : 2}
for k in d: #by default iterating a dict produces keys
    print(k)

#other dict iterations
for v in d.values():
    print(v)
for k in d.keys():
    print(k)

with open("README.md") as f: #file iteration
    for line in f:
        print(line)


