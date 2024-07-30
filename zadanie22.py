multipl = 1
i = 1
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    multipl *= i
    i += 1
print(multipl)
