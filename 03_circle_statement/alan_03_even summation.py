# even summation

print("sum of evens in 0-100: ")
i = 100         # i=1-100
sum_1 = 0
while i > 0:
    c = i % 2     # %
    if c == 0:
        sum_1 += i
        print(i)
    i -= 1
    if i == 0:
        print(i)
print("sum of evens in 0-100 are %d." % sum_1)

