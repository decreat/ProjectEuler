firstValue = 1
secondValue = firstValue + firstValue
fib = firstValue + secondValue
sum = 0

array = []
array.append(firstValue)
array.append(secondValue)
array.append(fib)

while fib < 2000000:
    firstValue = fib + secondValue
    secondValue = firstValue + fib
    fib = firstValue + secondValue
    array.append(firstValue)
    array.append(secondValue)
    array.append(fib)
        
print (array)

for i in array:
    if (i < 4000000 and i%2 == 0):
        sum += i
        print (i, sum)
