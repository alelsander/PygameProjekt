c = input()
s = "map/" + c + ".txt" 
f = open(s, "r")
e = []
for i in f:
    e.append(i.split(", "))
for i in e:
    print(i)
