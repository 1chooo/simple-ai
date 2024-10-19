def return_values():
    values = [1, 2, 3, 4]
    return *values,

a, b, c, d = return_values()
print(a, b, c, d)  # 輸出：1 2 3 4

