lst = [0] * 6
num = int(input())

t = num

for i in range(6):
    lst[i] = t
    t += 2
print(lst)

# s = int(input())
#
# arr = []
#
# while len(arr) < 6:
#     arr.append(s)
#     s += 2
#
# print(arr)

# s = "ATCKB"
#
# for i in range(4, -1, -1):
#     for j in range(0, i + 1):
#         print(s[j], end='')
#     print()

# for i in range(5):
#     for j in range(i, 4+1):
#         print(s[j], end = '')
#     print()

#
# arr = [
#     [s] for _ in range(5)
# ]
# i = 0
# arr1 = [
#     [s] for _ in range(len(arr))  if len(arr) >= 0
# ]
#
# print(arr)
# print(arr1)
# arr = [
#     list(map(int, input().split())) for _ in range(3)
# ]
#
# de = -1
# print(arr)

# arr = [
#     [3, 2, 7, 5],
#     [1, 7, 1, 7],
#     [1, 2, 3, 4]
# ]
#
# flag = False
#
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if arr[i][j] == 7:
#             flag = True
#             break
#     if flag == 1:
#         break
#
# if flag == 0:
#     print("안존재")
# else:
#     print("존재")

# arr = [3, 2, 7, 5, 3, 7, 1]
#
# flag = False
# for i in range(len(arr)):
#     if arr[i] == 7:
#         flag = True
#         break
#
# if flag == 0:
#     print("안존재")
# else:
#     print("존재")


# arr = [
#     [3, 2, 5, 9],
#     [1, 2, 3, 4],
#     [5, 5, 7, 7],
# ]
# 
# cnt = 0
# 
# # r c
# # i j
# # x y
# 
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         if 3 <= arr[i][j] and arr[i][j] <= 4:
#             cnt += 1

# print(cnt)

# arr = [3, 4, 5, 7, 7, 7, 5]

# cnt = 0
# for i in arr:
#     if i == 7:
#         cnt += 1
#
# print(cnt)
# cnt = 0
# i = 0
# while i < len(arr):
#     arr[i] == 7
#     cnt += 1
#     i += 1
# print(cnt)

# cnt = 0
# for i in arr:
#     if i % 2 != 0:
#         cnt += 1
#
# print(cnt)
