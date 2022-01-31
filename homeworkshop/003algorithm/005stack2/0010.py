# bit 반복문
N = 3
arr = [1, 2, 3]

sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
        return
    for i in range(2):
        sel[idx] = i
        powerset(idx+1)


powerset(0)