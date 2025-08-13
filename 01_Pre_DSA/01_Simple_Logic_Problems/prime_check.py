n = 30

for i in range(1, n+1):
    if i <= 1:
        continue
    is_prime = True
    
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, "is Prime")