
# q.1 - simple
lst = [5, 3, 2]
histo = ['*' * val for val in lst]
print(histo)

# q.2 - simple
f_lst = ["a", "b", "c"]
s_lst = ["x", "y", "z"]
lst_res = []

for i in range(0, len(f_lst)):
    lst_res.append(f_lst[i] + s_lst[len(f_lst) - 1 - i])

print(lst_res)

