
N =4

for i in range(1 << N):
    for j in range(N):
        if i & (1 << j):
            print()

print(5 & 3)

print(8 & 11)
