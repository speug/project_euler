x = 1
y = 1
curr = x
c = 0
s = 0
while(curr<4000000):
    curr = x + y
    if(c == 0):
        x = curr
        c = 1
    else:
        y = curr
        c = 0
    if(curr%2 == 0):
        s = s + curr
print(s)
