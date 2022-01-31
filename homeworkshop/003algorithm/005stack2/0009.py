# bit
N = 3
arr = [1, 2, 3]

sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
        return
    # 뽑고 가고
    sel[idx] = 1
    powerset(idx+1)
    # 안뽑고 가고
    sel[idx] = 0
    powerset(idx+1)

powerset(0)