x = 1
y = 0
while x < 1000:
    if (x%3==0 or x%5==0):
        y += x
        print (x, y)
    x += 1