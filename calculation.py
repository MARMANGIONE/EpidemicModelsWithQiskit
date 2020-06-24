t = 5
x = 0.134
a=0.98
numbers=[]
for i in range(1,6):
    numbers.append(x*(a**(i-1)))
print(numbers)
reduction = []
for n in numbers:
    reduction.append(1-n)
total = 1
for r in reduction:
    total = total * r
print(total)