s = list(input())
n = len(s) # κΈμμ
print(s)
# swap
for i in range(n//2):
    # s[i] <-> s[n-1-i]
    s[i], s[n-1-i] = s[n-1-i], s[i]
print(s)

# algorithm
# ['a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm']
# ['m', 'h', 't', 'i', 'r', 'o', 'g', 'l', 'a']